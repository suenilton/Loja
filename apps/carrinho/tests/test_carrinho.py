import pytest
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
from products.tests.factories import ProductFactory

from  ..carrinho import Carrinho

pytestmark = pytest.mark.django_db


def dummy_get_response(request):
    return None


@pytest.fixture
def http_request():
    request = HttpRequest()
    middleware = SessionMiddleware(dummy_get_response)
    middleware.process_request(request)
    return request


@pytest.fixture
def session(http_request):
    return http_request.session


@pytest.fixture
def carrinho(http_request, session):
    carrinho = Carrinho(http_request)
    session.modified = False
    return carrinho


def test_create_empty_carrinho(http_request, session):
    assert session.get(settings.CART_SESSION_ID) is None
    Carrinho(http_request)
    assert session[settings.CART_SESSION_ID] == {}


def test_get_non_empty_carrinho(http_request, session):
    session[settings.CART_SESSION_ID] = {"1": {}}
    Carrinho(http_request)
    assert session[settings.CART_SESSION_ID] == {"1": {}}


def test_add_product_to_empty_carrinho(product, carrinho, session):
    carrinho.add(product)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 1, "price": str(product.price)}
    }
    assert session.modified


def test_add_product_to_empty_carrinho_quantity_gt_1(product, carrinho, session):
    carrinho.add(product, 2)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 2, "price": str(product.price)}
    }
    assert session.modified


def test_add_product_to_empty_carrinho_twice(product, carrinho, session):
    carrinho.add(product)
    session.modified = False

    carrinho.add(product, 2)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 3, "price": str(product.price)}
    }
    assert session.modified


def test_add_product_to_empty_carrinho_override_quantity(product, carrinho, session):
    carrinho.add(product)
    session.modified = False

    carrinho.add(product, 4, override_quantity=True)

    assert session[settings.CART_SESSION_ID] == {
        str(product.id): {"quantity": 4, "price": str(product.price)}
    }
    assert session.modified


def test_remove_product(product, carrinho, session):
    carrinho.add(product)
    session.modified = False

    carrinho.remove(product)
    assert session[settings.CART_SESSION_ID] == {}
    assert session.modified


def test_remove_product_not_in_carrinho(product, carrinho, session):
    carrinho.remove(product)
    assert session[settings.CART_SESSION_ID] == {}
    assert not session.modified


def test_carrinho_iter(carrinho, session):
    p1 = ProductFactory()
    p2 = ProductFactory()
    p3 = ProductFactory()

    carrinho.add(p1)
    carrinho.add(p2, 2)
    carrinho.add(p3, 3)
    session.modified = False

    products = [p1, p2, p3]
    quantities = [1, 2, 3]

    for product, quantity, item in zip(products, quantities, carrinho):
        assert product.price == item["price"]
        assert product.price * quantity == item["total_price"]
        assert product == item["product"]
        assert "update_quantity_form" in item

    assert not session.modified
    assert list(carrinho.carrinho.values()) != list(iter(carrinho))


def test_carrinho_length(carrinho):
    p1 = ProductFactory()
    p2 = ProductFactory()

    assert len(carrinho) == 0

    carrinho.add(p1)
    assert len(carrinho) == 1

    carrinho.add(p2, 3)
    assert len(carrinho) == 4


def test_get_total_price(carrinho):
    p1 = ProductFactory()
    p2 = ProductFactory()

    carrinho.add(p1)
    carrinho.add(p2, 2)

    total_price = (p1.price * 1) + (p2.price * 2)

    assert carrinho.get_total_price() == total_price


def test_cant_add_more_than_max_items(product, carrinho):
    carrinho.add(product, settings.CART_ITEM_MAX_QUANTITY)
    assert len(carrinho) == settings.CART_ITEM_MAX_QUANTITY

    carrinho.add(product, 1)
    assert len(carrinho) == settings.CART_ITEM_MAX_QUANTITY
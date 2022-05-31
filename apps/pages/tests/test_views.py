import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def home_response(client):
    return client.get(reverse("pages:home1"))


@pytest.fixture
def about_response(client):
    return client.get(reverse("pages:about1"))


class TestHomePageView:
    def test_reverse_resolve(self):
        assert reverse("pages:home1") == "/pages/"
        assert resolve("/pages/").view_name == "pages:home1"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, r"pages\home1.html")


class TestAboutView:
    def test_reverse_resolve(self):
        assert reverse("pages:about1") == "/pages/about/"
        assert resolve("/pages/about/").view_name == "pages:about1"

    def test_status_code(self, about_response):
        assert about_response.status_code == 200

    def test_template(self, about_response):
        assertTemplateUsed(about_response, r"pages\about1.html")
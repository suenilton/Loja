from django.urls import path
from .views import AboutPageView, HomePageView

app_name = 'pages'

urlpatterns =[
    path("", HomePageView.as_view(), name="home1"),
    path("about/", AboutPageView.as_view(), name="about1"),
]
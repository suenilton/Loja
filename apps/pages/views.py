from django.shortcuts import render

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages\home1.html"


class AboutPageView(TemplateView):
    template_name = r"pages\about1.html"

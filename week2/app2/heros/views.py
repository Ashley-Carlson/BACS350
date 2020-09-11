from django.views.generic import TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"

class IndexView(TemplateView):
    template_name = "index.html"

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse

class TemplateView(TemplateView):
    template_name = "index.html"

class DetailView(TemplateView):
    template_name = "detail.html"

class CreateView(TemplateView):
    template_name = "create.html"

class UpdateView(TemplateView):
    template_name = "update.html"

class DeleteView(TemplateView):
    template_name = "delete.html"

class IndexView(TemplateView):
    template_name = "index.html"

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from os.path import exists
from .models import Superhero
from django.http import HttpResponse

class DetailView(DetailView):
    template_name = "detail.html"
    model = Superhero

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/' + image):
            kwargs['missing'] = True
        return kwargs


class ListView(ListView):
    template_name = "index.html"
    model = Superhero


class AddView(CreateView):
    template_name = "add.html"
    model = Superhero
    fields = '__all__'


class EditView(UpdateView):
    template_name = "edit.html"
    model = Superhero
    fields = '__all__'

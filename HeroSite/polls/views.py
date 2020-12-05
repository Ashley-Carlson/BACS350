from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from os.path import exists
from .models import Superhero
from .forms import SuperheroAddForm, RegisterForm
from django.http import HttpResponse


class DetailView(DetailView):
    template_name = "detail.html"
    model = Superhero

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs["object"].image
        if not exists("/" + image):
            kwargs["missing"] = True
        return kwargs


class ListView(ListView):
    template_name = "index.html"
    model = Superhero


class AccordionView(ListView):
    template_name = "accordion.html"
    model = Superhero


class TabsView(ListView):
    template_name = "tabs.html"
    model = Superhero


class TableView(ListView):
    template_name = "table.html"
    model = Superhero


class ContactView(ListView):
    template_name = "contact.html"
    model = Superhero


class AboutView(ListView):
    template_name = "about.html"
    model = Superhero


class AddView(CreateView):
    template_name = "add.html"
    form_class = SuperheroAddForm
    success_url = "/"


class EditView(UpdateView):
    template_name = "edit.html"
    model = Superhero
    fields = "__all__"


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"

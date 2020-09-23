from django.views.generic import TemplateView
from django.http import HttpResponse

class GinsburgView(TemplateView):
    template_name = "ginsburg.html"

class OkoyeView(TemplateView):
    template_name = "okoye.html"
    
class ElectraView(TemplateView):
    template_name = "electra.html"

class HarleyView(TemplateView):
    template_name = "harley.html"

class SheraView(TemplateView):
    template_name = "shera.html"

class IndexView(TemplateView):
    template_name = "index.html"

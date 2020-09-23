"""Project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from heros.views import SheraView, ElectraView, GinsburgView, IndexView, HarleyView, OkoyeView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("shera", SheraView.as_view(), name="shera"),
    path("harley", HarleyView.as_view(), name="harley"),
    path("electra", ElectraView.as_view(), name="electra"),
    path("okoye", OkoyeView.as_view(), name="okoye"),
    path("ginsburg", GinsburgView.as_view(), name="ginsburg"),
]

urlpatterns += staticfiles_urlpatterns()

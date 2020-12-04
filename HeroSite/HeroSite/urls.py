"""HeroSite URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from polls.views import (
    AddView,
    DetailView,
    EditView,
    ListView,
    AboutView,
    ContactView,
    DetailView,
    RegisterView,
)

urlpatterns = [
    #    path('', HeroView.as_view()),
    #    path('<str:identity>', HeroView.as_view()),
    path("", ListView.as_view(), name="hero_list"),
    path("about", AboutView.as_view(), name="about"),
    path("<int:pk>", DetailView.as_view(), name="detail"),
    path("add", AddView.as_view(), name="add"),
    path("contact", ContactView.as_view(), name="contact"),
    path("<int:pk>/", EditView.as_view(), name="hero_edit"),
    path("admin/", admin.site.urls),
    path("register", RegisterView.as_view(), name="register"),
    path("", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

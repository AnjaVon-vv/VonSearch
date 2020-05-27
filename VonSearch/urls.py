"""VonSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from search.views import SearchSuggest, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view(), name="index"),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('suggestions/', SearchSuggest.as_view(), name="suggestions"),
    path('search/', SearchView.as_view(), name="search"),
]


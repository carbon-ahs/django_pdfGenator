from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from core import views


# from .views import say_hello

urlpatterns = [
    path("", views.pdf_view, name="home"),
    path("home/", views.home, name="home1"),
]

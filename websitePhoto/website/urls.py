from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gallery/", views.gallery, name="gallery"),
    path("detailPhoto/<str:pk>/", views.detailPhoto, name="detailPhoto"),
]

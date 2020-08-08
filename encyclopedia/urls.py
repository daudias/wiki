from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search", views.search, name="search"),
    path("create", views.createNewPage, name="createNewPage"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("wiki/<str:title>/edit", views.editPage, name="editPage")
]

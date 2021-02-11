from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("new_entry", views.add, name="new_entry"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("search", views.search, name="search")
]


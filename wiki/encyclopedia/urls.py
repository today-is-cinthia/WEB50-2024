from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="wiki"),
    path("search/", views.search, name="search"),
    path("create", views.create_new_page, name="create"),
    path("edit/<str:title>", views.edit_page, name="edit"),
    path("random", views.random_entry, name="random_entry")
]

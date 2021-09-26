from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Fill all entries in index page
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("wiki/<str:entry>/edit", views.edit, name="edit"),
    path("random_page", views.random_page, name="random"),
]
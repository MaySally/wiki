from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search_entries, name="search"),
    path("random", views.random_entry, name="random"),
    path("new", views.new_page, name="newpage"),
    path("create_new", views.create_new, name="create_new"),
    path("<str:entry>", views.entry_title, name="entry_title")]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry_title, name="entry_title"),
    path("search", views.search_entries, name="search")]

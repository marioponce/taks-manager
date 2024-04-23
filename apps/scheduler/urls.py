from django.urls import path
from . import views, api

# VIEW URLS
urlpatterns = [
    path("", views.people, name ="home"),
    path("delete_person/<int:person_id>/", views.delete_person, name = "delete_person"),
    path("edit_person/<int:person_id>/", views.edit_person, name = "edit_person"),
    path("add_person/", views.add_person, name = "add_person"),
]

# API URLS
urlpatterns += [
    path("post_person/", api.post_person, name = "post_person"),
]
from django.urls import path 

from .views import (
    home, contact_view,
)


app_name = "pollapp"
urlpatterns = [
    path("", home, name="home"),
    path("contact-us/", contact_view, name="contact_view"),
]

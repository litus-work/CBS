from main.views.views import IndexPage, AboutUsPage, InfoPage, ContactsPage
from django.urls import path

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("info/", InfoPage.as_view(), name="info"),
    path("contacts/", ContactsPage.as_view(), name="contacts"),
    path("about/", AboutUsPage.as_view(), name="about"),
]
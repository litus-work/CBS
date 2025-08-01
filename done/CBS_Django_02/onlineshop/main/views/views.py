from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from main.views import BaseSimplePage
from articles.data import articles

class IndexPage(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        return {
            "categories": list(articles.keys())
        }

class InfoPage(BaseSimplePage):
    page_content = (
        "Welcome to our news platform. We deliver reliable and up-to-date news from around the world. "
        "Stay informed with our coverage of current events, politics, technology, and more."
    )
    page_name = "Info"
    page_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs9vztg4DuPoq5xdt5qLI5OF5EYUVtGqpmmw&s"

class AboutUsPage(BaseSimplePage):
    page_content = (
        "We are a team of passionate journalists and editors dedicated to bringing you honest and accurate news. "
        "Our mission is to inform, educate, and inspire our readers every day."
    )
    page_name = "About Us"
    page_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs9vztg4DuPoq5xdt5qLI5OF5EYUVtGqpmmw&s"

class ContactsPage(BaseSimplePage):
    page_content = (
        "Have questions or feedback? We'd love to hear from you. "
        "Email us at contact@newstoday.com or call us at +1-800-NEWS-123."
    )
    page_name = "Contacts"
    page_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs9vztg4DuPoq5xdt5qLI5OF5EYUVtGqpmmw&s"
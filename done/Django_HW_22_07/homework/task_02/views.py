from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "task_02/home.html"


class LukeView(TemplateView):
    template_name = "task_02/luke.html"


class LeiaView(TemplateView):
    template_name = "task_02/leia.html"


class HanView(TemplateView):
    template_name = "task_02/han.html"

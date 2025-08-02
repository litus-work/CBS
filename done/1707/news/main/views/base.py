from django.http import HttpRequest
from django.views.generic import TemplateView

class BaseSimplePage(TemplateView):
    template_name = "main/simple_page.html"
    page_name = ""
    page_content = ""
    page_image = ""

    def get_context_data(self, **kwargs):
        return {
            "title": self.page_name,
            "content": self.page_content,
            "image": self.page_image
        }
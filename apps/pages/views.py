from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "apps/pages/home.html"


class AboutView(TemplateView):
    template_name = "apps/pages/about.html"

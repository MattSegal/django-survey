from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = "landing.html"


landing = LandingView.as_view()

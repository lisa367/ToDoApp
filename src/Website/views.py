from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import SignUpForm


User = get_user_model()


class LandingPageView(TemplateView):
    template_name = "landing_page.html"


class SignUpView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy("ToDo:home", )
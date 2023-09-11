from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    # redirect_authenticated_user = True
    success_url = '/astrologer/login'

    def get_success_url(self):
        user = self.request.user
        if user.role == 'astrologer':
            return reverse('astrologer_dashboard')
        elif user.role == 'translator':
            return reverse('translator_dashboard')
        elif user.role == 'customer':
            return reverse('customer_dashboard')


class AstrologerDashboardView(LoginRequiredMixin, TemplateView):
    print('pppppppp')
    template_name = 'astrologer_dashboard.html'


class TranslatorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'translator_dashboard.html'


class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'customer_dashboard.html'


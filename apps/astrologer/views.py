from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.db.models import Count

from apps.conversation.models import Conversation


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def post(self, request):
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)

        user = auth.authenticate(request, email=email, password=password)
        # print(user.role)

        if user is not None:
            login(request, user)
            print("User Role: 1st", user.role)
            if user.role == 'Astrologer':
                print("astrology")
                return redirect('conversations')
            elif user.role == 'translator':
                print("translator")
                return redirect('translator_dashboard')
            elif user.role == 'customer':
                print("customer")
                return redirect('customer_dashboard')

        else:
            print('user is None')

        # Handle invalid login credentials here
        return super().post(request)


class AstrologerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'webchat/astrologer_dashboard.html'


class ConversationListView(LoginRequiredMixin, ListView):
    template_name = 'webchat/astrologer_dashboard.html'
    queryset = Conversation.objects.all().prefetch_related('messages')
    context_object_name = 'conversations'

    def get_template_names(self):
        if self.request.is_ajax():
            pass
        # ['webchat/api_conversation.html']
        return super().get_template_names()

    def get_context_data(self, *agrs, **kwargs):
        ctx = super().get_context_data(*agrs, **kwargs)

        selected = self.request.GET.get('conversation')

        selected_obj = None
        if not selected:
            selected_obj = self.get_queryset().filter(id=selected).first()

        if not selected_obj:
            selected_obj = self.get_queryset().first()

        ctx['selected'] = selected_obj
        return ctx

    def get_queryset(self):
        return super().get_queryset().filter(
            astrologer__user=self.request.user
        )


class TranslatorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'translator_dashboard.html'


class CustomerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'customer_dashboard.html'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('home'))
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponseNotFound

from apps.conversation.models import Message


class TranslatorDashboardView(LoginRequiredMixin, ListView):
    template_name = 'translator/dashboard.html'
    queryset = Message.objects.prefetch_related('conversation')
    context_object_name = 'messages'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'Translator':
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(
            conversation__translator=self.request.user,
            translated_content__isnull=True
        ).order_by('created_at')


class MessageTranslateView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'Translator':
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk):
        message = Message.objects.get(pk=pk)
        message.translated_content = request.POST.get('translated_content')
        message.save()
        return redirect('translator_dashboard')
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.conversation.models import Message


class TranslatorDashboardView(LoginRequiredMixin, ListView):
    template_name = 'translator/dashboard.html'
    queryset = Message.objects.all().prefetch_related('conversation')
    context_object_name = 'messages'
    paginate_by = 5

    # def get_queryset(self):
    #     return super().get_queryset().filter(
    #         conversation__translator=self.request.user,
    #         translated_content__isnull=True
    #     ).order_by('created_at')
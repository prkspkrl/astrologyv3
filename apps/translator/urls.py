from django.urls import path
from . import views
from .views import TranslatorDashboardView, MessageTranslateView

urlpatterns = [
    path('dashboard/', TranslatorDashboardView.as_view(), name='translator_dashboard'),
    path('message/<int:pk>/', MessageTranslateView.as_view(), name='message_translate'),
]
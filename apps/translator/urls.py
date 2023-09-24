from django.urls import path
from . import views
from .views import TranslatorDashboardView

urlpatterns = [
    path('dashboard/', TranslatorDashboardView.as_view(), name='translator_dashboard'),
]
from django.urls import path
from .views import CustomLoginView
from . import views
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='astrologer-login'),
    path('astrologer_dashboard/', views.AstrologerDashboardView.as_view(), name='astrologer_dashboard'),
    path('translator_dashboard/', views.TranslatorDashboardView.as_view(), name='translator_dashboard'),
    path('customer_dashboard/', views.CustomerDashboardView.as_view(), name='customer_dashboard'),
]
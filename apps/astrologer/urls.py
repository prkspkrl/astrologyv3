from django.urls import path
from .views import CustomLoginView, AstrologerDashboardView, ConversationListView, TranslatorDashboardView, CustomerDashboardView, LogoutView
from . import views
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='astrologer-login'),
    # path('astrologer_dashboard/', AstrologerDashboardView.as_view(), name='astrologer_dashboard'),
    path('conversations/', ConversationListView.as_view(), name='conversations'),
    path('translator_dashboard/', TranslatorDashboardView.as_view(), name='translator_dashboard'),
    path('customer_dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
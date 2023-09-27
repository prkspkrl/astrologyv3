from django.urls import path
from .views import CustomLoginView, AstrologerDashboardView, ConversationListView, CustomerDashboardView, LogoutView
from . import views
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='astrologer-login'),
    # path('astrologer_dashboard/', AstrologerDashboardView.as_view(), name='astrologer_dashboard'),
    path('conversations/', ConversationListView.as_view(), name='conversations'),
    path('customer_dashboard/', CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
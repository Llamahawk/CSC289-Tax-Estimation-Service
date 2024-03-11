from django.urls import path
from .views import MainView, LoginView, SignUpView, DashboardView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

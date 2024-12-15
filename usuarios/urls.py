from django.urls import path
from .views import RegistroView
from .views import LoginView
urlpatterns = [
    path('register/', RegistroView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

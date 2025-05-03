from django.urls import path

from . import views
from . import functions

urlpatterns = [
    path('google/redirect', views.google_redirect, name='google_redirect'),
    path('google/callback', views.google_callback, name='google_callback'),
    path('google/token_callback', functions.token_callback, name='google_token_callback'),
]
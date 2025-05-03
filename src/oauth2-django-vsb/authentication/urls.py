from django.urls import path

from . import views

urlpatterns = [
    path('google/redirect', views.google_redirect, name='google_redirect'),
    path('google/callback', views.google_callback, name='google_callback'),
    path('logout_view', views.logout_view, name='logout_view'),
]
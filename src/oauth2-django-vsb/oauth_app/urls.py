from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_login, name='site_login'),
    path('login', views.site_login, name='site_login'),
    path('home', views.site_index, name='site_index'),
    path('implementation', views.site_implementation, name='site_implementation'),
    path('googleCloud', views.site_googleCloud, name='site_googleCloud'),

]

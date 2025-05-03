from django.urls import path

from . import views

urlpatterns = [
    path('', views.site_login, name='site_login'),
    path('login', views.site_login, name='site_login'),
    path('home', views.site_index, name='site_index'),
    path('history', views.site_history, name='site_history'),
    path('details', views.site_tech_details, name='site_details'),
    path('tests', views.site_tests, name='site_tests'),
    path('results', views.site_results, name='site_results'),
    path('others', views.site_other_tools, name='site_othertools'),
    path('orchestration', views.site_orchestration, name='site_orcherstration'),
]

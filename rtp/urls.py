from django.urls import path
from . import views

app_name = 'rtp'

urlpatterns = [
    path('', views.search , name='search'),
    path('search_sma/', views.search_sma , name='search_sma'),
    path('search_big6/', views.search_big6 , name='search_big6'),
    path('search_dodo/', views.search_dodo , name='search_dodo'),
    path('rtp_bunyang/', views.bunyang_data, name='bunyang'),
    path('rtp_salesma/', views.salesma_data, name='salesma'),
    path('rtp_salebig6/', views.salebig6_data, name='salebig6'),
    path('rtp_saledodo/', views.saledodo_data, name='saledodo'),

]
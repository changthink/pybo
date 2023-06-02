from django.urls import path
from . import views

app_name = 'ahome'

urlpatterns = [
    path('', views.apply_base , name='apply_base'),
    path('pjmanage/', views.pj_list , name='pj_list'),
    path('<int:abase_id>/', views.apply_detail , name='apply_detail'),
    path('ibju/', views.ibju_data , name='ibju_list'),
    path('onsale/', views.onsale_data , name='onsale_list'),
    path('pop/', views.pop_data , name='pop_list'),
    path('const/', views.const_data , name='const_list'),
    path('pjcode/', views.pjcode_data , name='pjcode_list'),
    path('rtech/', views.rtech_data, name='rtech_list'),
    path('img/', views.img_data, name='img_list'),
    path('table/', views.table_data, name='table_list'),
    path('tbl_kb50/', views.tbL_kb50, name='tbl_kb50'),
    path('tbl_pir/', views.tbl_pir, name='tbl_pir'),
    path('tbl_floorarea/', views.tbl_floorarea, name='tbl_floorarea'),
    path('tbl_allpj/', views.tbl_allpj, name='tbl_allpj'),
    path('rtp_bunyang/', views.rtp_bunyang, name='rtp_bunyang'),

]
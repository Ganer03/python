from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_case, name='create_case'),
    path('<int:case_id>/', views.case_detail, name='case_detail'),
    path('<int:case_id>/update/', views.update_case, name='update_case'),
    path('create_client/', views.create_client, name='create_client'),
    path('client_list/', views.client_list, name='client_list'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/<int:client_id>/update/', views.update_client, name='update_client'),
    path('area_list/', views.area_list, name='area_list'),
    path('area/<int:area_id>/', views.area_detail, name='area_detail'),


]
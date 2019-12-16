from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.doctor_form,name='doctor_insert'), 
    path('<int:id>/', views.doctor_form,name='doctor_update'), 
    path('delete/<int:id>/',views.doctor_delete,name='doctor_delete'),
    path('list/',views.doctor_list,name='doctor_list') 
]
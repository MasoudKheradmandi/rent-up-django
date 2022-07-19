from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.home, name='home'),
    path('listaparteman/', views.list_view_aparteman, name='list_view_apa'),
    path('listvila/', views.list_view_vila, name='list_view_vila'),
    path('detailvila/<int:id>', views.detail_view_vila, name='detailvila'),
    path('savepost/',views.savepost,name='savepost'),
]

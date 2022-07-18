from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list_view_aparteman, name='list_view'),
    path('detail/', views.detailview, name='detail'),
    path('savepost/',views.savepost,name='savepost')
]

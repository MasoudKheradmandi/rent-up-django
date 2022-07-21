from django.urls import path
from . import views

app_name = 'admin_informations'

urlpatterns = [
    path('listagent',views.agent_list,name='listagent'),
    path('detailagent/<id>/',views.agent_detail,name='detailagent'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('mypro/',views.MyProperty,name='mypro'),
]

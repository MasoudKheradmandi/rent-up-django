from django.urls import path
from . import views

app_name = 'admin_informations'

urlpatterns = [
    path('listagent',views.agent_list,name='listagent'),
    path('detailagent/<int:id>',views.agent_detail,name='detailagent'),
]

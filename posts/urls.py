from django.urls import path
from . import views


urlpatterns = [
    path('',views.save_post_apa,name='save_post_apa'),
    path('villa/',views.save_post_villa,name='save_post_villa'),
    path('zamin/',views.save_post_zamin,name='zamin')
]

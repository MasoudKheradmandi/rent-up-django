from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    path('',views.save_post,name='save_post'),
    path('aparteman/',views.save_post_apa,name='save_post_apa'),
    path('villa/',views.save_post_villa,name='save_post_villa'),
    path('zamin/',views.save_post_zamin,name='save_post_zamin')
]

from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    path('',views.save_post,name='save_post'),
    path('aparteman/',views.save_post_apa,name='save_post_apa'),
    path('villa/',views.save_post_villa,name='save_post_villa'),
    path('zamin/',views.save_post_zamin,name='save_post_zamin'),
    path('compare/<noe>/<int:id>',views.compare_post_f,name='compare_post_f'),
    path('ctc/<noe>',views.choose_to_compare,name='choose_to_compare'),
    path('compare/<first_noe>/<int:first_id>/<int:seconed_id>',views.compare_post_t,name='compare_post_t'),
]

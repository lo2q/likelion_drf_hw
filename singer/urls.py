from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "singer"

urlpatterns = [
    path('tags/<str:tags_name>', views.find_tag),
    path('', views.singer_list),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('<int:singer_id>/song', views.song_read_create),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

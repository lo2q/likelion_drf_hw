from django.urls import path
from . import views

app_name = "singer"

urlpatterns = [
    path('', views.singer_list),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('<int:singer_id>/song', views.song_read_create),
]

from django.urls import path
from django.views.generic.base import TemplateView
from .views import RoomList,RoomDetail,CreateRoom,RoomUpdate,RoomDelete

urlpatterns = [
    path('rooms/', TemplateView.as_view(template_name="rooms/ajax.html"), name='room_main'),
    path('rooms/list', RoomList.as_view(), name='room_list'),
    path('rooms/create', CreateRoom.as_view(), name='room_create'),
    path('rooms/update/<int:pk>', RoomUpdate.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>', RoomDelete.as_view(), name='room_delete'),
    path('rooms/<int:pk>', RoomDetail.as_view(), name='room_detail'), 
]
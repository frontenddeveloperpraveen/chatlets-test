from django.urls import path
from . import views
urlpatterns = [
    path('home',views.Home,name="Home"),
    path('chat',views.Chat,name="chat"),
    path('check-room',views.Check_room,name="check-room"),
    path('<str:room>/',views.Room_join,name="check-room"),
    path('send',views.Send,name="Send"),
    path('getMessages/<str:room>/',views.message,name="Message"),
    path('download',views.Download,name="download"),
    path("",views.Page,name="Page")
]

from django.contrib import admin
from django.urls import path, include

from home import views
from .views import starting, PostListView, about

urlpatterns = [
    path('', PostListView.as_view(), name='home-home'),
    # path('create/', ModelCreateView.as_view(), name="home-createpost"),
    # path('update/<int:pk>/s', ModelUpdateView.as_view(), name="home-updatepost"),
    # path('detail/<int:pk>/', postdetails, name="home-detailpost"),
    # path('detail/<int:pk>/commentsubmit/', views.commentsubmit, name="home-commentsubmit"),
    # path('detail/<int:pk>/likepost/', views.likepost, name="home-likepost"),
    # path('delete/<int:pk>/', ModelDeleteView.as_view(), name="home-deletepost"),
    # path('user/<str:username>/', UserListView.as_view(), name="home-user"),
    path('about/', about, name='home-about'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('user/<str:username>/', views.userchat, name='user-room'),
]
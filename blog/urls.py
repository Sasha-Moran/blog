from django.urls import path

from .views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('tags/<str:slug>', posts_with_tag, name='post_with_tag'),
    path('logout/', user_logout, name='logout')
]

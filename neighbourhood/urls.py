from django.urls import path
from .views import PostCreateView
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('posts/',views.post,name='posts'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create')
]
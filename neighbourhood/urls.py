from django.urls import path

from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('posts/',views.post,name='posts')
]
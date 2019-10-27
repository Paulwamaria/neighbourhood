from django.urls import path
from .views import PostCreateView,BusinessCreateView,PostUpdateView,PostDeleteView
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('posts/',views.post,name='posts'),
    path('business/',views.business_list,name='business'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('business/new/',BusinessCreateView.as_view(), name = 'business-create'),
    path('profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
]
from django.urls import path
from .views import PostCreateView,NotificationCreateView,BusinessCreateView,PostUpdateView,PostDeleteView, BusinessDeleteView, BusinessUpdateView
from . import views


urlpatterns=[
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('posts/',views.post,name='posts'),
    path('business/',views.business_list,name='business'),
    path('post/new/',PostCreateView.as_view(), name = 'post-create'),
    path('notification/new/',NotificationCreateView.as_view(), name = 'notification-create'),
    path('business/new/',BusinessCreateView.as_view(), name = 'business-create'),
    path('profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('business/<int:pk>/update/',BusinessUpdateView.as_view(), name = 'business-update'),
    path('business/<int:pk>/delete/',BusinessDeleteView.as_view(), name = 'business-delete'),
    path('search/',views.search_results, name = 'search_results'),
]
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('u/<str:username>/',UserPostListView.as_view(),name="user-view"),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name="post-edit"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    path('post/new/',PostCreateView.as_view(),name="post-create"),
    path('about/',views.about,name="blog-about")
]


from django.urls import path
from .views import  PublishAuthors, PostsById, PostsView

urlpatterns = [
    # path('', PublishedPostsView.as_view()),
    path('', PostsView.as_view()),
    path('posts/<int:pk>', PostsById.as_view()),


]

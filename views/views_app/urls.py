from django.urls import path

from . import views
from .views import PostsById, PostsView, CreateAutorView, AuthorList, AuthorDetail,\
    UpdateAuthorView, DeleteAuthorViews, CreateCategoryView, DeleteCategoryView, UpdateCategoryView, CategoryList, CategoryDetail, paginator_view

urlpatterns = [
    # path('', PublishedPostsView.as_view()),
    path('', views.MainPage.as_view(), name='main_page'),

    path('posts/<int:pk>', PostsById.as_view()),
    path('authors/create/', CreateAutorView.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    path('authors/<int:pk>/update/', UpdateAuthorView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', DeleteAuthorViews.as_view(), name='author_delete'),

    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/create/', views.CreatePostView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/update/', views.UpdatePostView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),


    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/detail', CategoryDetail.as_view(), name='category_detail'),
    path('category/create', CreateCategoryView.as_view(), name='category_create'),
    path('category/<int:pk>/delete', DeleteCategoryView.as_view(), name='delete_category'),
    path('category/<int:pk>/update', UpdateCategoryView.as_view(), name='category_update'),

    path('paginator_authors/', views.paginator_view)


]

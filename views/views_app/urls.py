from django.urls import path

from .views import PostsById, PostsView, CreateAutorView, AuthorList, AuthorDetail,\
    UpdateAuthorView, DeleteAuthorViews, CreateCategoryView, DeleteCategoryView, UpdateCategoryView, CategoryList, CategoryDetail

urlpatterns = [
    # path('', PublishedPostsView.as_view()),
    path('', PostsView.as_view()),
    path('posts/<int:pk>', PostsById.as_view()),
    path('authors/create/', CreateAutorView.as_view(), name='author_create'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    path('authors/<int:pk>/update/', UpdateAuthorView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', DeleteAuthorViews.as_view(), name='author_delete'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/detail', CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/create', CreateCategoryView.as_view(), name='category_create'),
    path('category/<int:pk>/delete', DeleteCategoryView.as_view(), name='delete_category'),
    path('category/<int:pk>/update', UpdateCategoryView.as_view(), name='category_update'),
    # path('category/')

]

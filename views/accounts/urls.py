from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('change_password/done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', views.SignUpView.as_view(), name='user_register')

]

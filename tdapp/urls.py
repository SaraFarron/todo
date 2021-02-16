from django.urls import path
from . import views


app_name = 'tdapp'
urlpatterns = [
    path('', views.index, name='home'),

    path('create/', views.create_task, name='create'),
    path('update/<str:pk>', views.update_task, name='update'),
    path('delete/<str:pk>', views.delete_task, name='delete'),

    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_page, name='register'),
    path('user/', views.profile_page, name='profile'),
]
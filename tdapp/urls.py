from django.urls import include, path
from . import views


app_name = 'tdapp'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_task, name='create'),
    path('update/<str:pk>', views.update_task, name='update'),
    path('delete/<str:pk>', views.delete_task, name='delete'),
]
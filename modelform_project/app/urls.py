from django.urls import path
from app import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('create/', views.blog, name='create'),
    path('update/<int:id>', views.update_blog, name='update'),
    path('delete/<int:id>', views.delete_blog, name='delete'),
]
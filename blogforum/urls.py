from django.urls import path
from . import views
from .views import PostCreate

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('category/<int:category_id>/',
         views.PostsByCategory.as_view(), name='posts_by_category'),
]

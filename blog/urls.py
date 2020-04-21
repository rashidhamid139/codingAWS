from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path('create/', views.ArticleCreateView.as_view(),  name='artice-create'),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(),  name='artice-delete'),
    path('<int:id>/update/', views.ArticleUpdateView.as_view(),  name='artice-update'),
    path('', views.ArticleListView.as_view(),  name='article-list'),
    path('<int:id>/', views.ArticleDetailView.as_view(),  name='article-detail')
]
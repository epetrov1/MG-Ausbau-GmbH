from django.urls import path, include
from .views import BlogDetailView, BlogListView



urlpatterns = [
    path('<slug:slug>/', BlogDetailView.as_view(), name="detail_projects"),
    path('', BlogListView.as_view(), name="projects"),
]
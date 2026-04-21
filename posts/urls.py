from django.urls import path
from .views import PostListView, PostDetailView, EditProfileView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('<int:id>/', PostDetailView.as_view(), name='post_detail'),
]
from django.urls import path
from .views import post_list, post_detail, edit_profile

urlpatterns = [
    path('', post_list, name='post_list'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('<int:id>/', post_detail, name='post_detail'),
]
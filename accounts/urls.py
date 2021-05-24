from django.urls import path
from .views import login_view, logout_view, register_view, update_view, delete_view, contact



urlpatterns = [
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('register/', register_view, name='register_url'),
    path('update/', update_view, name='update_url'),
    path('delete/', delete_view, name='delete_url'),
    path('contact/', contact, name='contact_url'),
]
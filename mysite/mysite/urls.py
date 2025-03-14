from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import LoginView and LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Your blog app URLs
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Correct login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Correct logout view
]

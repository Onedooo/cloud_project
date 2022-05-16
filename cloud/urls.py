"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from cloud import views

urlpatterns = [
    path('', views.main, name='main'),
    path('useredit/<int:pk>', views.user_edit, name='user_edit'),
    path('fileupload', views.file_upload, name='file_upload'),
    path('detail/<int:pk>', views.file_detail, name='file_detail'),
    path('edit/<int:pk>', views.file_edit, name='file_edit'),
    path('remove/<int:pk>', views.file_remove, name='file_remove'),
    path('commentadd/<int:pk>', views.add_comment, name='add_comment'),
    path('removecom/<int:pk>', views.remove_comment, name='remove_comment'),
    # path('guestadd/<int:pk>', views.guest_add, name='guest_add'),

    path('login/', auth_views.LoginView.as_view(template_name='cloud/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='sign_up'),
]

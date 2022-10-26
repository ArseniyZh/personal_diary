"""personalDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from diary import views as dv
from users import views as uv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dv.index, name='index'),
    path('profile/', dv.profile, name='profile'),
    path('edit_profile', uv.edit_profile, name='edit_profile'),
    path('create_post', dv.create_post, name='create_post'),
    path('my_posts', dv.my_posts, name='my_posts'),
    re_path(r'^delete_post/(?P<pk>\d+)$', dv.DeletePost.as_view(), name='delete_post'),
    re_path(r'^update_post/(?P<pk>\d+)$', dv.UpdatePost.as_view(), name='update_post'),

    path('login', uv.user_login, name='login'),
    path('logout', uv.user_logout, name='logout'),
    path('sign_up', uv.sign_up, name='sign_up'),
]

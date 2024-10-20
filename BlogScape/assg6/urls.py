"""
URL configuration for assg6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from blogs.views import home, write, blog_detail, search
from user.views import register, profile
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name = 'BlogPage'),
    path('search/',search, name = 'SearchPage'),
    path('writetheblog', write, name = 'WriteBlogPage'),
    path('blog/<int:blog_id>/', blog_detail, name='BlogDetail'),
    path('register/',register, name='RegisterPage'  ),
    path('profile/<str:username1>/',profile, name='ProfilePage'  ), 
    path('', auth_view.LoginView.as_view(template_name ='user/login.html'), name='LoginPage'),
    path('logout/', auth_view.LogoutView.as_view(template_name ='user/logout.html'), name='LogoutPage')
]


from django.conf.urls.static import static
from django.conf import  settings


if settings.DEBUG:
    
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


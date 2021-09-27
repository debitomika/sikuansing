"""sikuansing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.urls.conf import include
from django.conf.urls.static import static
from accounts import views as accounts_views
from backend import views as backend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/loggout.html'), name='logout'),
    path('profil/', accounts_views.profil, name='profil'),
    path('tidakdiizinkan/', backend_views.tidak_diizinkan, name='tidak-diizinkan'),
    path('editprofil/<int:pk>', accounts_views.edit_profil, name='edit-profil'),

    path('ganti_passsword/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
        name='ganti_password'),
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), 
        name='password_change_done'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'backend.views.error_403'
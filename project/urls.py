"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as authViews

#from eypeeay.views import *
from userapp.views import *
from app.views import *
from eypeeay.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #-------API------
	path('userAPI/<str:name>/', userAlbumAPI, name ='profile-api'),
    path('albumAPI/', albumAPI, name ='album-api'),
	#-------first------
	path('a/', admin.site.urls, name ='admin'),
	path('profile/', profiles, name ='profile'),
	path('', homeList, name ='home'),
	path('search/', searchPerson, name ='home-search'),
	#-------album------
	path('album/<int:apk>/', albumDetail, name ='album-detail'), 
	path('album/delete/<int:apk>/', albumDelete, name ='album-delete'), 
	#-------photo------
	path('album/<int:apk>/upload/', uploadImage, name ='upload-photo'),
	path('album/<int:apk>/upload/photos/', showImages, name ='photo-list'), #redirect after the upload
	path('album/<int:apk>/photos/', showImages, name ='photos'),
	path('photo/<int:ipk>/', imageDetail, name ='photo-detail'),
	path('photo/<int:ipk>/update/', updateImages, name ='update-photo'),
	path('photo/<int:ipk>/delete/', deleteImages, name ='delete-photo'),
	path('album/<int:apk>/delete/photos', showImages, name ='from-delete'), #redirect after the delete
	#-------user------
	path('login/', authViews.LoginView.as_view(template_name='userlogin.html'), name ='login'),
	path('logout/', authViews.LogoutView.as_view(template_name='userlogout.html'), name ='logout'),
	path('register/', registerUser, name ='register'),
	path('update/', updateUser, name ='user-update')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

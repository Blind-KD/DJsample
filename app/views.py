from django.contrib.auth.models import User
from userapp.models import *
from userapp.forms import *
from django.shortcuts import render, redirect, get_object_or_404 as go404
from django.contrib.auth.decorators import login_required

@login_required
def homeList(request):
    if request.method == 'POST':
        name = album.objects.create(author=request.user)
        name.albumName = request.POST.get('album')
        name.save()
        return redirect('home') 

    alb = album.objects.all().order_by('-dateTime')
    context = { 
            'alb':alb,
    }
    return render(request, 'home.html', context)

#-------------search--------------
@login_required
def searchPerson(request):
    id = User.objects.get(username=request.GET.get('search'))
    searched = profile.objects.filter(profileName=id)
    context = {
         'searched':searched,
    }
    return render(request, 'home_search.html', context)

#-------------profile--------------
@login_required
def profiles(request):
      profile_pk = profile.objects.get(profileName=request.user)
      album_pk = album.objects.filter(author=request.user).order_by('-dateTime')
      context = { 
            'alb':album_pk,
            'pro':profile_pk
	  }
      return render(request, 'profile.html', context) 

#-------------album--------------
@login_required
def albumDetail(request, apk):
    if request.method == 'POST': 
        name = album.objects.filter(id=apk).update(albumName=request.POST.get('update'))
       

    album_pk = album.objects.get(id=apk)
    context = {
			'apk':album_pk,
    }
    return render(request, 'album_detail.html', context)

@login_required
def albumDelete(request, apk):
    album_pk = album.objects.get(id=apk)
    if request.method == 'POST':
        album_pk.delete()
        return redirect('home')
    context = {
			'apk':album_pk,
    }
    return render(request, 'album_delete.html', context)

#-------------photo--------------
@login_required
def showImages(request, apk):
    album_pk = album.objects.get(id=apk)
    photos = photo.objects.filter(photoAlbum=album_pk).order_by('-id')
    context = { 
            'apk':album_pk,
            'img':photos,
	  }
    return render(request, 'photo_list.html', context)

@login_required
def uploadImage(request, apk):
    album_pk = album.objects.get(id=apk)
    if request.method == 'POST':
        form  = uploadForm(request.POST, request.FILES)
        if form.is_valid():
              form.instance.album_id = apk
              form.instance.photoAlbum = album_pk
              form.save()
              return redirect('photos/')
    else:
          form = uploadForm()
    context = {
			'form':form,
            'apk':album_pk,
    }
    return render(request, 'upload_photo.html', context)

@login_required
def imageDetail(request, ipk):
    photo_pk = photo.objects.get(id=ipk)
    context = { 
            'img':photo_pk,
    }
    return render(request, 'photo_detail.html', context)

@login_required
def updateImages(request, ipk):
    photo_pk = photo.objects.get(id=ipk)
    if request.method == 'POST': 
        form  = imageForm(request.POST, instance=go404(photo, id = ipk))
        if form.is_valid():
              form.save()
              return redirect('photo-detail')
    else:
          form = imageForm()
    context = {
			'form':form,
            'ipk':photo_pk,
    }
    return render(request, 'update_photo.html', context)

@login_required
def deleteImages(request, ipk):
    photo_pk = photo.objects.get(id=ipk)
    if request.method == 'POST':
        photo_pk.delete()
        return redirect('from-delete',apk=photo_pk.photoAlbum.id)
    context = {
			'ipk':photo_pk,
    }
    return render(request, 'photo_delete.html', context)

 
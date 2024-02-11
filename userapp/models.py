from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class profile(models.Model):
	profileName = models.OneToOneField(User, on_delete=models.CASCADE)
	profilePic = models.ImageField(default='d.jpg', upload_to='profilePic')
	
	def __str__(self):
		return f'{self.profileName}'
	
class personRequest(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.sender}'

class persons(models.Model):
	personName = models.ForeignKey(User, on_delete=models.CASCADE)
    
	def __str__(self):
		return f'{self.personName}'

class album(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	albumName = models.CharField(max_length=100, unique=True)
	dateTime = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.albumName}'

	def get_absolute_url(self):
		return reverse('album-detail', kwargs={'apk':self.pk})
    	
class photo(models.Model):
	photoAlbum = models.ForeignKey(album, on_delete=models.CASCADE, blank=True)
	photoName = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photoAlbum/images')
	imgDescription = models.TextField(max_length=500)

	def __str__(self):
		return f'{self.photoName}'
	
	def get_absolute_url(self):
		return reverse('photo-detail', kwargs={'ipk':self.pk}) 
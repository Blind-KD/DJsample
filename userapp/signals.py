from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile, personRequest, persons

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
	if created:
		profile.objects.create(profileName=instance)
		
@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
	instance.profile.save()

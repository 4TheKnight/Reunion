from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
import os

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    image = models.ImageField(upload_to='Profilepic/',blank=True)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='friend_list')

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_delete,sender=Profile)
def delete_profile_image_file(sender, instance,**kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Status/',blank=True)
    desciption = models.TextField()
    likes = models.ManyToManyField(Profile,related_name='likes',blank=True)

    def __str__(self):
        return self.desciption

@receiver(pre_delete,sender=post)
def delete_post_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class comments(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'Comment by {self.author} <br> {self.comment}' if self.comment else 'No content provided'

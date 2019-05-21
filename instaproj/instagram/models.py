# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Image(models.Model): 
  photo_image = models.ImageField(upload_to = "images/")
  caption = models.TextField()
  profile = models.ForeignKey('Profile',on_delete=models.deletion.CASCADE,)
  likes = models.IntegerField()
  comments = models.TextField()

  def save_image(self):

    self.save()
  
  def delete_image(self):

    Image.objects.get(id = self.id).delete()
  def update_caption(self,val):
    Image.objects.filter(id = self.id).update(caption = val)
  
  @classmethod
  def search_by_name(cls,search_term):

    uname= cls.objects.filter(profile__name__icontains=search_term)
    return uname

  def __str__(self):
    return self.caption
 
class Profile(models.Model):
  name = models.CharField(max_length = 250)
  profile_photo = models.ImageField(upload_to = "images/")
  bio = models.TextField()

  def save_profile(self):
    self.save()
  
  def delete(self):
    Profile.objects.get(id = self.id).delete()
  
  def update(self,field,val):
    Profile.objects.get(id=self.id).update(field=val)
    

  def __str__(self):
    return self.bio


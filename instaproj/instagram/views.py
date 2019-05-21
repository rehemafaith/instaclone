# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Profile 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required


@login_required(login_url= "/accounts/login/")
def home(request):
  image = Image.objects.all()

#   for image in images:

  


  return render(request,'index.html',{"image":image})

@login_required
def search(request):

   if 'insta_search' in request.GET and request.GET["insta_search"]:
      searched = request.GET.get("insta_search")
      if searched:
         user = User.objects.filter(username=searched).first()

   context = {
      'searched': searched,
      'user': user
   }

   return render(request, 'timeline/search.html', context)

def profile(request):
   profile = Profile.objects.all()

   return render (request,'profile.html',{"profile":profile})


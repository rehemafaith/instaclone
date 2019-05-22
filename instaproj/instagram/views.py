# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Profile 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ImageForm, ProfileForm

@login_required(login_url= "/accounts/login/")
def home(request):
  image = Image.objects.all()

#   for image in images:

  


  return render(request,'index.html',{"image":image})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def profile(request):
   profile = Profile.objects.all()

   return render (request,'profile.html',{"profile":profile})

def like(request,image_id):

   user = request.user

   image = Image.objects.filter(pk=image_id).first()
   like = image.like_set.filter(liked_by=user.profile).first()
   

   if like:
      like.delete()
   else:
      Like.likes(image,user.profile)

   return redirect('home')


@login_required(login_url='/accounts/login/')  
def add_image(request):
    user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = user
            image.save()
            return redirect("index")
    else:
        form = ImageForm()
    return render(request, "add_image.html", {"form": form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_bio = form.cleaned_data['bio']
            new_pic = form.cleaned_data['pic']
            profile = Profile.objects.get(user=request.user)
            profile.bio = new_bio
            profile.pic = new_pic
            profile.save()
            final_url = "/update/" + str(request.user.id) + "/"
            return redirect(final_url)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form": form})

@login_required(login_url='/accounts/login/')
def comment(request):
    image_id = request.POST.get("id")
    image = Image.objects.get(pk=image_id)
    Comments.objects.create(user=request.user, image=image,
                            comm=request.POST.get("comment"))

    user = request.user.username
    comment = request.POST.get("comment")

    data = {"user": user, "comment": comment}
    return JsonResponse(data)
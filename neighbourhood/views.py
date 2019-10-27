from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post
from users.models import Profile

def index(request):
    message = " Whats Going on in your Neighbourhood?"
    neighborhoods = Neighborhood.objects.all()


    context = {
        "message":message,
        "neighs":neighborhoods,
      
    
    }

    return render(request,'neighbourhood/index.html',context)


@login_required
def post(request):
  
    profile=Profile.objects.get(user=request.user)
    posts = Post.objects.filter(neighborhood__neighborhood_name=profile.location)

    

    context={
        "posts":posts
    }

    return render(request,'neighbourhood/posts.html',context)
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post,Business
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



class PostCreateView(LoginRequiredMixin,CreateView):
     
    model = Post
    success_url = ('/')
    fields = ['title','image','content']

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.neighborhood = Neighborhood.objects.get(neighborhood_name = self.request.user.profile.location)
        return super().form_valid(form)

class BusinessCreateView(LoginRequiredMixin,CreateView):
     
    model = Business
    success_url = ('/')
    fields = ['business_name','logo','description','business_email']

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.instance.neighborhood = Neighborhood.objects.get(neighborhood_name = self.request.user.profile.location)
        return super().form_valid(form)


@login_required
def business_list(request):
  
    profile=Profile.objects.get(user=request.user)
    businesses = Business.objects.filter(neighborhood__neighborhood_name=profile.location)

 

    context={
        "businesses":businesses
    }

    return render(request,'neighbourhood/businesses.html',context)



def display_profile(request,username):
    profile = Profile.objects.get(user__username= username)

    user_posts = Post.objects.filter(user =profile.user).order_by('created_on')

    context={
        "profile":profile,
        "user_posts":user_posts
    }
    return render(request,'neighbourhood/profile_detail.html',context)






class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     
    model = Post

    fields = ['title','image','content']


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()

        if self.request.user == post.user:
            return True

        return False

    def get_redirect_url(self,pk, *args, **kwargs):
        obj = get_object_or_404(Post, pk = pk)
        url= obj.get_absolute_url()
      
      
        return url


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = ('/')
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.user:
            return True

        return False



class BusinessUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     
    model = Business

    fields = ['business_name','logo','description','business_email']


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        business = self.get_object()

        if self.request.user == business.user:
            return True

        return False

    def get_redirect_url(self,pk, *args, **kwargs):
        obj = get_object_or_404(Business, pk = pk)
        url= obj.get_absolute_url()
      
      
        return url


class BusinessDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Business
    success_url = ('/')
    def test_func(self):
        business = self.get_object()

        if self.request.user == business.user:
            return True

        return False



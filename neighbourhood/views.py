from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Post,Business,Notification, EmergencyContact
from users.models import Profile



def about(request):
    return render(request,'neighbourhood/about.html')


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
    notifications = Notification.objects.filter(neighborhood__neighborhood_name=profile.location)
    contacts = EmergencyContact.objects.filter(neighborhood__neighborhood_name=profile.location)
  
    

    context={
        "posts":posts,
        "notifications":notifications,
        "contacts":contacts
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

class NotificationCreateView(LoginRequiredMixin,CreateView):
     
    model = Notification
    success_url = ('/')
    fields = ['content']

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
    notifications = Notification.objects.filter(neighborhood__neighborhood_name=profile.location)
    contacts = EmergencyContact.objects.filter(neighborhood__neighborhood_name=profile.location)

 

    context={
        "businesses":businesses,
        "notifications":notifications,
        "contacts":contacts
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
    success_url = ('/')
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





def search_results(request):
    if 'search_business' in request.GET and request.GET["search_business"]:
        search_term = request.GET.get("search_business")
        
        searched_businesses = Business.objects.filter(business_name__icontains=search_term)
        message=search_term
        return render(request, "neighbourhood/search.html", {"businesss":searched_businesses, "message":message})

    else:
        message = "Search term not found"

        return render(request,'neighbourhood/search.html',{"message":message})



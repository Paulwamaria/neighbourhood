from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NeighborhoodRegistrationForm, UserUpdateForm, ProfileUpdateForm,ChangeNeighborhoodForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile



def register(request):
    if request.method == 'POST':
        form = NeighborhoodRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            messages.success(request, f'Account created for {username}')
            return redirect('profile')
    else:
        form = NeighborhoodRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)    
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance = request.user)
        
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)



@login_required
def change_neighborhood(request):
    if request.method == 'POST':
        n_form = ChangeNeighborhoodForm(request.POST,instance = request.user.profile)
        
          
        if n_form.is_valid():
            n_form.save()
         
    else:
        n_form = ChangeNeighborhoodForm(instance = request.user.profile)
        
      


    context={
        'n_form':n_form,
      
    }
    return render(request, 'users/change_hood.html',context)

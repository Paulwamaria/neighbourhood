from django.shortcuts import render
from .forms import NeighborhoodRegistrationForm

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



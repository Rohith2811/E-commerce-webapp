from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html',{'user_form':user_form, 'profile_form':profile_form})

def logout_view(request):
    logout(request)
    return redirect('home:index')


def profile(request):
    if  request.user.is_authenticated:
        profile = Profile.objects.get(user_id = request.user.id)
        return render(request, 'users/profile.html', {"profile":profile} )
    else:
        return redirect('login')
    
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        data = ProfileForm(request.POST, instance=profile)
        if data.is_valid():
            data.save()
            return redirect('profile')
    form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {"form":form})
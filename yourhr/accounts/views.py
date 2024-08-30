# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')
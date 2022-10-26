from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, SignUpForm, EditProfileForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'diary/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            rp = request.POST
            username = rp['username']
            password = rp['password1']
            first_name = rp['first_name']
            last_name = rp['last_name']

            user = authenticate(username=username, password=password)

            profile = Profile()
            profile.user = user
            profile.first_name = first_name
            profile.last_name = last_name
            profile.save()

            login(request, user)
            return HttpResponseRedirect('/')

    else:
        form = SignUpForm()
    return render(request, 'diary/sign_up.html', {'form': form})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()

            rp = request.POST
            profile.first_name = rp.get('first_name')
            profile.last_name = rp.get('last_name')
            profile.bio = rp.get('bio')
            profile.save()

            return HttpResponseRedirect('profile')
    else:
        form = EditProfileForm()
        form.fields['first_name'].initial = profile.first_name
        form.fields['last_name'].initial = profile.last_name
        form.fields['bio'].initial = profile.bio

    return render(request, 'diary/edit_profile.html', {'form': form})

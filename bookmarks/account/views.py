from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'],
                                )
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse('authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            if user is None:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def nameView(request):
    return HttpResponse("Hello, World!")


@login_required
def dashboard(request):
    user = request.user
    return render(request, 'account/dashboard.html', {'section': 'dashboard','user':user})


class PasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'


def register(request):
    user_form = UserRegisterForm()
    if request.method == 'POST':
        new_user_form = UserRegisterForm(request.POST)
        if new_user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = new_user_form.save(commit=False)
            # Set the chosen password
            # this set_passsword will also encrypt the password
            new_user.set_password(new_user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # this will redirect the user to success page
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            return render(request, 'account/register_done.html', {'new_user': user_form})

    else:
        return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

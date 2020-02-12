from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, UserAccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def index(request):

    context = {}
    return render(request, 'user_accounts/account_profile.html', context)


def register(request):
    loggedin = False
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_account_form = UserAccountForm(data=request.POST)

        if user_form.is_valid() and user_account_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_account_form.save(commit=False)
            profile.user = user

            # Handling the profile photo
            if 'profile_photo' in request.FILES:
                profile.profile_photo = request.FILES['profile_photo']
            profile.save()

            registered = True
            loggedin = True
        else:
            print(user_form.errors, user_account_form.errors)

    else:
        user_form = UserForm()
        user_account_form = UserAccountForm()


# This will be injected into the HTML template
    context = {
        'user_form': user_form,
        'user_account_form': user_account_form,
        'registered': registered,
        'loggedin': loggedin,
    }

    return render(request, 'user_accounts/register.html', context)


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("This Account is not active, Please contact the support Team!")
        else:
            print("Someone tried to login and faild!")
            print(f"username: {username} \nPassword: {password}")
            return HttpResponse("INVALID LOGIN DETAILS")
    else:
        return render(request, 'user_accounts/login.html')

    context = {}
    return render(request, 'user_accounts/login.html', context)

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

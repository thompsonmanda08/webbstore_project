from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm, UserAccountForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth

# Create your views here.


def index(request):

    context = {}
    return render(request, 'user_accounts/account_profile.html', context)

# User Registrations using Django modelForms (NOT FUNCTIONAL!!!)
def register_old(request):
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
    }

    return render(request, 'user_accounts/register.html', context)

# User Registrations using Bootstrap forms designed in HTML file (FUNCTIONAL)
def register(request):

    if request.method == 'POST': # User has submitted info and wants an account
        username = request.POST['username']
        email = request.POST['email']

        if request.POST['password1'] == request.POST['password2']: # Password Validation

            try: # This is likely to fail if both email and username are not in database!
                user = models.User.objects.get(username=username)
                context = {
                    'error': 'Username/Email already exists! Try a new one!'
                        }
                return render(request, 'user_accounts/register_.html', context)

            except (User.DoesNotExist):
                user = models.User.objects.create_user(username=request.POST['username'],
                                                       password=request.POST['password2'],
                                                       email=request.POST['email'],
                                                       first_name=request.POST['first_name'],
                                                       last_name=request.POST['last_name'],)

                # After creating the user we want to log them into their account!

                auth.login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'user_accounts/register_.html', {'password_error': "Passwords Don't match! Try again!"})
    else:
        return render(request, 'user_accounts/register_.html')



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

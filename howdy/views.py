# -*-coding: utf-8 -*-
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import render, redirect
# from . import models
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.contrib.auth import login, authenticate
# from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# from .models import *

# for search function
from wagtail.core.models import Page
from wagtail.search.models import Query
from .forms import *

def homepage(request):

    template = get_template('index.html')
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def test(request):

    context = {
        'var': 'value'
    }
    return render(request, 'test.html', context)

def about(request):

    context = {
        'var': 'value'
    }
    return render(request, 'about.html', context)

def post(request):

    context = {
        'var': 'value'
    }
    return render(request, 'post.html', context)

# mortgage calculator

def mortgage_calculator(request):

    context = {
        'var': 'value'
    }
    return render(request, 'mortgagecalc/mortgage_calculator.html', context)

# user registration

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                return render(request, 'index.html', {})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'email_reg/login.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('email_reg/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration.')
            # return render(request, 'email_reg/acc_active_sent.html')
    else:
        form = SignupForm()
    return render(request, 'email_reg/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, ObjectDoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def logout(request):
    pass
    return redirect('/')


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return render(request, 'email_reg/upload_success.html')


def display_hotel_images(request):

    if request.method == 'GET':

        Hotels = Hotel.objects.all()
        return render(request, 'display_hotel_images.html', {'hotel_images': Hotels})

def search(request):
    # Search
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search_index/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })

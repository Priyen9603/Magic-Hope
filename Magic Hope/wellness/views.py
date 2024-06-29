from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.db.utils import IntegrityError
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Order
from .forms import OrderForm

from django.shortcuts import render

import json
import time
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.shortcuts import render

import socket
from django.shortcuts import render

import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

import urllib.parse
import os
import time
import base64
import random
from django.core.mail import send_mail
from django.conf import settings
import random
import string

import csv


from .forms import UserProfileForm

api_key = 'AtMEJrgh3shmlJsw0efNEgxZKVMFEIiO'
def home(request):
    return render(request, 'home.html')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile





@csrf_exempt
def SignupPage(request):
    error_message = None
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')

        # Check if email field is of type text
        if request.POST.get('email') == 'text':
            error_message = 'Email field should not be of type text.'
        else:
            # Check if email is valid
            try:
                EmailValidator()(email)
            except ValidationError as e:
                error_message = 'Please enter a valid email address.'

            # Check if email is already in use
            if User.objects.filter(email=email).exists():
                error_message = 'Email is already in use. Please use a different email.'
            else:
                try:
                    my_user = User.objects.create_user(uname, email, pass1)
                    my_user.save()
                    return redirect('login')
                except IntegrityError:
                    error_message = 'Username already exists. Please choose a different username.'

    return render(request, 'signup.html', {'error_message': error_message})


 


def LoginPage(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Incorrect password. Please try again.'
        else:
            error_message = 'Username not registered. Please signup.'

    return render(request, 'login.html', {'error_message': error_message})

@csrf_exempt
def HomePage(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        # If not authenticated, redirect to a login page or another appropriate location
        return redirect('/login')  # Adjust the redirect location as needed
    
    # If authenticated, render the home page
    return render(request, 'home.html')

def logout_view(request):
    django_logout(request)  # Log out the user
    return redirect('/login')  # Redirect to the login page



web_scraping_api_keys = [
    '68f78776c6mshc53ac8a3bad2a3ep17a962jsn6397b2e0c95f',
    '537941368bmsh72f6cc9ab972e3cp183ed3jsne0779c04ae58',
    '6c9378b829msh3f544d27ef7cf60p1bb3e1jsnbf80036f2374',
    '1e6e8fd435mshf0f755cfaeb7b76p16dfa9jsn8de297649131',
    '10c4ba8c9fmshbb108295bae9e88p1f0ad4jsnb0c67b9dea3c'
]
current_api_key_index = 0
def get_next_api_key():
    global current_api_key_index
    current_api_key_index = (current_api_key_index + 1) % len(web_scraping_api_keys)
    return web_scraping_api_keys[current_api_key_index]


def about(request):
    return render(request,'about.html')  # Render the "About" page

def services(request):
    return render(request,'services.html')  # Render the "Services" page

def contact(request):
    return render(request,'contact.html')  # Render the "Contact" page


# wellness/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


# wellness/views.py


def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        view_mode = request.GET.get('edit') != 'true'
        form = UserProfileForm(instance=request.user.profile)

    context = {
        'form': form,
        'view_mode': view_mode,
    }
    return render(request, 'profile_view.html', context)

# wellness/views.py


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                user=request.user,
                course=course,
                amount=course.price,
                status='Pending'
            )
            return redirect('payment')  # Redirect to payment page
    else:
        form = OrderForm()
    return render(request, 'course_detail.html', {'course': course, 'form': form})

def payment(request):
    # Payment logic will be integrated here (e.g., Stripe or PayPal)
    return render(request, 'payment.html')

# wellness/views.py

import stripe
from django.conf import settings
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def create_payment_intent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=1000,  # Replace with actual course price
                currency='usd',
                payment_method=data['payment_method_id'],
                confirmation_method='manual',
                confirm=True,
            )
            return JsonResponse({'client_secret': payment_intent.client_secret})
        except stripe.error.CardError as e:
            return JsonResponse({'error': str(e)}, status=400)

# wellness/views.py

from django.shortcuts import render, get_object_or_404
from .models import Course
from django.conf import settings
import stripe
import json

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})

# wellness/views.py

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        payment_method_id = data.get('payment_method_id')

        try:
            intent = stripe.PaymentIntent.create(
                amount=5000,  # The amount to charge, in cents
                currency='usd',
                payment_method=payment_method_id,
                confirmation_method='manual',
                confirm=True,
            )
            return JsonResponse({'client_secret': intent.client_secret})
        except stripe.error.CardError as e:
            return JsonResponse({'error': str(e)}, status=400)
# wellness/views.py

from django.shortcuts import render

def thank_you(request):
    return render(request, 'thank_you.html')
from django.http import JsonResponse
from .models import Counselor, Appointment
from .forms import AppointmentForm


def home1(request):
    counselors = list(Counselor.objects.all())

    # Add pre-defined therapists
    predefined_therapists = [
        {'id': 1001, 'name': 'Dr. Jane Smith', 'speciality': 'Cognitive Behavioral Therapy',
         'image': 'https://picsum.photos/300/200?random=1'},
        {'id': 1002, 'name': 'Dr. John Doe', 'speciality': 'Family Counseling',
         'image': 'https://picsum.photos/300/200?random=2'},
        {'id': 1003, 'name': 'Dr. Emily Brown', 'speciality': 'Trauma Therapy',
         'image': 'https://picsum.photos/300/200?random=3'},
        {'id': 1004, 'name': 'Dr. Michael Lee', 'speciality': 'Addiction Counseling',
         'image': 'https://picsum.photos/300/200?random=4'},
    ]

    counselors.extend(predefined_therapists)

    return render(request, 'home1.html', {'counselors': counselors})

from django.shortcuts import render, get_object_or_404
from .models import Counselor
from django.http import Http404

def book_appointment(request, counselor_id):
    try:
        counselor = Counselor.objects.get(id=counselor_id)
    except Counselor.DoesNotExist:
        # Handle pre-defined counselors
        pre_defined_counselors = {
            1001: {"name": "Dr. Jane Smith", "speciality": "Cognitive Behavioral Therapy"},
            1002: {"name": "Dr. John Doe", "speciality": "Family Counseling"},
            1003: {"name": "Dr. Emily Brown", "speciality": "Trauma Therapy"},
            1004: {"name": "Dr. Michael Lee", "speciality": "Addiction Counseling"},
        }

        if counselor_id in pre_defined_counselors:
            counselor = type('Counselor', (), pre_defined_counselors[counselor_id])
        else:
            raise Http404("Counselor does not exist")

    return render(request, 'book_appointment.html', {'counselor': counselor})


from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatResponse


def home3(request):
    return render(request, 'home3.html')


def get_response(request):
    if request.method == 'GET':
        question = request.GET.get('question', '').strip().lower()
        try:
            response = ChatResponse.objects.get(question=question)
            return JsonResponse({'response': response.response})
        except ChatResponse.DoesNotExist:
            return JsonResponse({'response': "I don't understand that question."})

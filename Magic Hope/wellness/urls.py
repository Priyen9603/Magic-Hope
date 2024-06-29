"""
URL configuration for avs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wellness import views
from .views import create_payment_intent


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.SignupPage, name='signup'),
   path('signup', views.SignupPage, name='signup'),
   path('login', views.LoginPage, name='login'),
   path('home',views.home,name="home"),
   path('logout/', views.logout_view, name='logout'),  # URL for the logout view
   path('about/', views.about, name='about'),  
   path('services/', views.services, name='services'),  
   path('contact/', views.contact, name='contact'),
   path('profile_view/', views.profile_view, name='profile_view'),
   path('course_list/', views.course_list, name='course_list'),
   path('course/<int:course_id>/', views.course_detail, name='course_detail'),
   path('payment/', views.payment, name='payment'),
   path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
   path('thank_you/', views.thank_you, name='thank_you'),
   path('book_appointment/<int:counselor_id>/', views.book_appointment, name='book_appointment'),
   path('home1/', views.home1, name='home1'),
   path('home3/', views.home3, name='home3'),
   path('get-response/', views.get_response, name='get_response'),

]

#    path('leakosint/', views.leakosint_integration, name='leakosint_integration'),
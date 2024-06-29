from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'phone_number', 'interests', 'goals', 'communication_styles']
        widgets = {
            'interests': forms.Textarea(attrs={'rows': 3}),
            'goals': forms.Textarea(attrs={'rows': 3}),
            'communication_styles': forms.Textarea(attrs={'rows': 3}),
        }


from django import forms
from .models import Course, Order

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
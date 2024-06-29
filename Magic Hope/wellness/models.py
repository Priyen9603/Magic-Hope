# wellness/models.py

from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, blank=True, null=True)  # Add name field
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add phone number field
    interests = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    communication_styles = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'
class Counselor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.counselor.name} - {self.date} {self.time}"


from django.db import models


class ChatResponse(models.Model):
    question = models.CharField(max_length=255)
    response = models.CharField(max_length=255)

    def __str__(self):
        return self.question

from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    emailAddress = models.EmailField(max_length=60)
    password = models.CharField(max_length=100)
    profession = models.CharField(max_length=60)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.profession}"


class Doctor(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    emailAddress = models.EmailField(max_length=60)
    password = models.CharField(max_length=100)
    workgroup = models.CharField(max_length=10)
    speciality = models.CharField(max_length=60)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.speciality}"


class Appointment(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    ref_code = models.CharField(max_length=20)
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="booked_appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name="appointments")
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.title}" 




    

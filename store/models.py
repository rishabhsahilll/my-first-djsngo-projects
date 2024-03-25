from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserDta(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwods = models.CharField(max_length=50)
    # forgenkey = models.ForeignKey()

    def __str__(self):
        return f"{self.fullname}"

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    education = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state_region = models.CharField(max_length=100)
    image = models.CharField(max_length=255, default='https://res.cloudinary.com/rishabh-insta/image/upload/v1711364015/media/y4kp4jeyxpfzhtud1mtg.png')  # Default URL

    def __str__(self):
        return f"{self.first_name} {self.surname}"
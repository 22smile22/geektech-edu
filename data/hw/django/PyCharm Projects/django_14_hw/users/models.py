from django.db import models

# Create your models here.
#hw7

from django.contrib.auth.models import User

class CustomUser(User):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )

    OCUP_CHOICE = (
        ("STUDENT", "Student"),
        ("WORKER", "Worker"),
        ("JOBLESS", "Jobless"),
        ("RETIRED", "Retired"),
        ("FREELANCE", "Freelance"),
        ("REMOTE", "Remote"),
    )
    EDUCATION = (
        ("BACHELOR", "Bachelor"),
        ("MASTER", "Master"),
        ("ENGINEER", "Engineer"),
    )
    phone_number = models.CharField("phone-number", max_length=60, unique=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Sex")
    age = models.IntegerField()
    occupation = models.CharField(choices=OCUP_CHOICE, max_length=80)
    secret_pass = models.CharField("maiden-name", max_length=60, unique=True)
    education = models.CharField(choices=EDUCATION, max_length=50)



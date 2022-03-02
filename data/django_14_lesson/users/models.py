from django.db import models

# Create your models here.
#ls7

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
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
        ("MILLIONAIRE", "MILLIONAIRE"),
    )
    phone_number = models.CharField("phone-number", max_length=60, unique=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")
    age = models.IntegerField()
    occupation = models.CharField(choices=OCUP_CHOICE, max_length=80)


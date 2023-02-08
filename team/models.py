from django.core.validators import RegexValidator
from django.db import models


class Role(models.TextChoices):
    REGULAR = 'RG',
    ADMIN = 'AD'

class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.REGULAR,
    )

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        
        user.save(using=self._db)
        my_group = Group.objects.get(name='Students') 
        my_group.user_set.add(user)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    phone = models.CharField(max_length=255, null=True)
    address_1 = models.CharField(max_length=255, null=True)
    address_2 = models.CharField(max_length=255, null=True)
    id_no = models.CharField(max_length=255, null=True)
    admission_no = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    sub_county = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",
                       "phone",
                       "address_1",
                       "address_2",
                       "id_no",
                       "admission_no",
                       "country",
                       "county",
                       "sub_county",
                       "location",
                       "gender",
                       #    "groups",

                       ]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

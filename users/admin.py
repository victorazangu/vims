from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email",
                    "username",
                    "first_name",
                    "last_name",
                    "is_staff",
                    "phone",
                    "address_1",
                    "address_2",
                    "id_no",
                    "admission_no",
                    "country",
                    "county",
                    "sub_county",
                    "location",
                    "gender",]


admin.site.register(CustomUser, CustomUserAdmin)

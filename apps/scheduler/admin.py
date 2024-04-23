from django.contrib import admin

from .models import Person, Aviability

admin.site.register(
    [
        Person,
        Aviability
    ]
)

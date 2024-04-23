from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    """Person's form"""

    class Meta:
        model = Person
        fields = [ # fields to be filled in the form
            "short_name",
            "name",
            "email",
            "role"
        ]
        labels = { # labels to display in the form instead of the field names
            "short_name": "Short name",
            "name": "Name",
            "email": "e-mail",
            "role": "Role"
        }

from django import forms
from django.core.exceptions import ValidationError


class NameForm(forms.Form):
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    your_name = forms.CharField(
        label='you name',
        max_length=100,
        initial="you name initial",
        label_suffix=" suffix",
        help_text="help_text",
        error_messages={
            "required": "please input you name"
        },
        disabled=True
    )
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    avatar = forms.DateField(widget=forms.Textarea())

    def clean_your_name(self):
        raise ValidationError("test error")

    def clean(self):
        raise ValidationError("clean form error")

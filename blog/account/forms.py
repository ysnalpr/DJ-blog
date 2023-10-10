from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput, validators=[validate_password]
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match")
        return cd["password2"]

    def clean_email(self):
        valid_domains = [
            "gmail.com",
            "yahoo.com",
            "hotmail.com",
            "live.com",
            "outlook.com",
        ]
        cd = self.cleaned_data
        domain = cd["email"].split("@")[-1]
        if domain not in valid_domains:
            raise forms.ValidationError("Enter a valid email")
        return cd["email"]

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Profile


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
        email = cd["email"]
        domain = cd["email"].split("@")[-1]
        if domain not in valid_domains or User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use or does not valid.")
        return email


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        cd = self.cleaned_data
        email = cd["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already in use.")
        return email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "date_of_birth", "bio"]

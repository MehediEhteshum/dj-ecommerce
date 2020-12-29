# check for unique email and username

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

non_allowed_usernames = ["abc"]


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )

    def clean_username(self):
        # some validation for username
        username = self.cleaned_data.get("username")
        # thisIsAUserName==thisisausername
        qs = User.objects.filter(username__iexact=username)
        if qs.exists() or username in non_allowed_usernames:
            raise forms.ValidationError(
                "Invalid username, please pick another.")
        return username

    def clean_email(self):
        # some validation for username
        email = self.cleaned_data.get("email")
        # thisIsAUserName==thisisausername
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     # validation for password possible here

    def clean_username(self):
        # some validation for username
        username = self.cleaned_data.get("username")
        # thisIsAUserName==thisisausername
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid username.")
        return username

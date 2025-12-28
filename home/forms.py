from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={"class":"form-control form-control-lg", "placeholder":"First name"}))
    last_name = forms.CharField(required=False, max_length=30, widget=forms.TextInput(attrs={"class":"form-control form-control-lg", "placeholder":"Last name"}))
    username = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={"class":"form-control form-control-lg", "placeholder":"Username"}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={"class":"form-control form-control-lg", "placeholder":"name@example.com"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap classes to password fields
        self.fields['password1'].widget.attrs.update({"class":"form-control form-control-lg", "placeholder":"Password"})
        self.fields['password2'].widget.attrs.update({"class":"form-control form-control-lg", "placeholder":"Confirm Password"})

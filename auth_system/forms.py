from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from auth_system.models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("phone_number", "first_name", "last_name", "email")

class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']


class PhoneNumberChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

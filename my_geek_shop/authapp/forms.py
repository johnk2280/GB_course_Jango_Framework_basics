from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            'username',
            'first_name',
            'password1',
            'password2',
            'email',
            'age',
            'avatar'
        )

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('You are too young')

        return age


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
            'username',
            'first_name',
            'email',
            'age',
            'avatar',
            'password'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            # if field_name == 'password':
            #     field.widget = forms.HiddenInput()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('You are too young')

        return age

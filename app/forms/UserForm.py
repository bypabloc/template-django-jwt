import crypt

from django import forms
from ..models import User

from .helpers import getErrorsFormatted

from datetime import date

class SignUpForm(forms.Form):

    nickname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    phone = forms.CharField(max_length=50, required=True)

    password = forms.CharField(max_length=150, required=True)
    password_confirmation = forms.CharField(max_length=150, required=True)

    state = forms.IntegerField(max_value=5, min_value=1, required=False)

    def clean(self):
        data = self.cleaned_data

        if 'nickname' in data:
            if User.objects.filter(nickname=data['nickname']).exists():
                self.add_error('nickname', 'Already exists')

        if 'email' in data:
            if User.objects.filter(email=data['email']).exists():
                self.add_error('email', 'Already exists')

        if 'phone' in data:
            if User.objects.filter(phone=data['phone']).exists():
                self.add_error('phone', 'Already exists')

        if 'password' in data and 'password_confirmation' in data:
            if data['password'] != data['password_confirmation']:
                self.add_error('password', 'The two password fields must match')
                self.add_error('password_confirmation', 'The two password fields must match')
        
        return data
        
    def _post_clean(self):
        super()._post_clean()

    def save(self):
        data = self.cleaned_data

        print('data', data)

        password_hashed = crypt.crypt(data['password']) # '$6$rounds=5000$saltstring$'
        print('password_hashed', password_hashed)

        data['password'] = password_hashed

        user = User.objects.create(**data)

        # del my_dict['key']

        return {}

    def getErrors(self):
        return getErrorsFormatted(self)


__author__ = 'Giri'
from django import forms
class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }
        )
    )
    username = forms.CharField(
        label="Enter User Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )
    password1 = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    password2 = forms.CharField(
        label="Enter Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email Id'
            }
        )
    )
    number = forms.IntegerField(
        label="Enter Your Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )

class LoginForm(forms.Form):
    username= forms.CharField(
        label='Enter Your YourName',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'UserName'
            }
        )
    )
    password1 = forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
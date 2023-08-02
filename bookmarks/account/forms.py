from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput,label='Password Input')
    password_confirmation = forms.CharField(max_length=20, widget=forms.PasswordInput,label='Password Confirmation')
    
    class Meta:
        model = User
        fields = ('username', 'first_name' , 'email',)
    
    def clean_password2(self):
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('password didn"t match')
        return pass2
    
    
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),required = True)
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}),required = True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}),required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),required = True)
    
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'user_name', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
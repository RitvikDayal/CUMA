from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from verify_email.email_handler import send_verification_email

def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            messages.success(request, f'Your acount have been created successfully. You can login now!')
            return redirect('login')
        else:
            messages.warning(request, f'Information entered is not vaalid!\nCheck details and try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
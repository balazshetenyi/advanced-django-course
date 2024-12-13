from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from . import forms


class LoginPage(View):
    form_class = forms.LoginForm
    login_path = 'authentication/login.html'
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.login_path, {'form': form, 'message': message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = "Invalid credentials"
        return render(request, self.login_path, {'form': form, 'message': message})


# def logout_user(request):
#     logout(request)
#     return redirect('login')
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

class AccountLoginView(LoginView):
    template_name = 'account/login.html'


class AccountLogoutView(LogoutView):
    template_name = 'account/logout.html'
    

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import *


class PasswordException(Exception):
    def __init__(self):
        super().__init__()


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'personalaccountapp/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'personalaccountapp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def change_password(request):
    user = None
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            user = User.objects.get(username=cleaned['username'])
            try:
                if user.check_password(cleaned["old_password"]):
                    if cleaned["old_password"] != cleaned["new_password"]:
                        user.set_password(cleaned["new_password"])
                        user.save()
                    else:
                        raise PasswordException()
            except PasswordException:
                form.add_error('new_password', 'Choose another password')
    else:
        form = ChangePasswordForm()
    context = {'form': form, 'user': user}
    return render(request, 'personalaccountapp/settings.html', context=context)

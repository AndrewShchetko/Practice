from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer, ResultsSerializer
from .forms import RegisterUserForm, LoginUserForm, ChangePasswordForm
from .models import Results, User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PasswordException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


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


class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = []

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


class LoginUserAPIView(APIView):
    # authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        form = LoginUserForm(data=request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'detail': f'Invalid form data: {form.cleaned_data}'}, status=status.HTTP_400_BAD_REQUEST)


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
                        raise PasswordException('Error')
            except PasswordException:
                form.add_error('new_password', 'Choose another password')
    else:
        form = ChangePasswordForm()
    context = {'form': form, 'user': user}
    return render(request, 'personalaccountapp/settings.html', context=context)


class ChangePasswordAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(request, data=request.data)

        if form.is_valid():
            cleaned = form.cleaned_data
            user = User.objects.get(username=cleaned['username'])

            try:
                if user.check_password(cleaned["old_password"]):
                    if cleaned["old_password"] != cleaned["new_password"]:
                        user.set_password(cleaned["new_password"])
                        user.save()
                        return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
                    else:
                        raise PasswordException('Choose another password')
                else:
                    raise PasswordException('Invalid old password')
            except PasswordException as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)


class ResultsModelViewSet(ReadOnlyModelViewSet):
    serializer_class = ResultsSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(self.request.user.username)
        queryset = Results.objects.filter(user=user)
        return queryset

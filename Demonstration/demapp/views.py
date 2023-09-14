from PIL import Image
import numpy as np
from tensorflow import keras
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import *


emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


class PasswordException(Exception):
    def __init__(self):
        super().__init__()


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'demapp/register.html'
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
    template_name = 'demapp/login.html'

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
    return render(request, 'demapp/settings.html', context=context)


def use_nn(request):
    user = request.user
    context = {'user': user}
    if request.method == 'POST':
        form = NeuralNetworkForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned = form.cleaned_data
            img = cleaned['image']
            image = Image.open(img).convert('L')
            width = image.size[0]
            height = image.size[1]
            pix = image.load()
            lst = []
            for y in range(height):
                for x in range(width):
                    color = pix[x, y]
                    lst.append(color)
            arr = np.array(lst)
            arr = np.reshape(arr, (48, 48))
            arr = arr / 255
            lst = arr.tolist()
            arr = np.array(lst)
            data = []
            data.append(arr)
            data = np.expand_dims(data, axis=3)
            model_loaded = keras.saving.load_model("./demapp/model")
            predicted = model_loaded.predict(data).tolist()
            maxi = predicted.index(max(predicted))
            emotion = emotions[maxi]
            context['image'] = image
            context['emotion'] = emotion
            context['comment'] = cleaned['comment']
            img_res = form.save()
            results = {'image': img_res, 'emotion': emotion, 'user': user}
            Results.objects.create(**results)
    else:
        form = NeuralNetworkForm()
    context['form'] = form
    return render(request, 'demapp/NNform.html', context=context)

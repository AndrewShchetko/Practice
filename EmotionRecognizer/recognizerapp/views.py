from PIL import Image
import numpy as np
from tensorflow import keras
from django.shortcuts import render
from .forms import *
from ..personalaccountapp.models import Results


emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


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
            model_loaded = keras.saving.load_model("./recognizerapp/model")
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
    return render(request, 'recognizerapp/NNform.html', context=context)

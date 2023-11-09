from PIL import Image
import numpy as np
from rest_framework.generics import CreateAPIView
from tensorflow import keras
from django.shortcuts import render
from .forms import *
from .image import resize_images
from personalaccountapp.models import Results
from personalaccountapp.serializers import ResultsSerializer
from .serializers import ImagesSerializer

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


def use_nn(request):
    user = request.user
    context = {'user': user}
    if request.method == 'POST':
        form = NeuralNetworkForm(request.POST, request.FILES)
        if form.is_valid():
            img_res = form.save()
            cleaned = form.cleaned_data
            img = cleaned['image']

            image = Image.open(img).convert('L')
            image = np.asarray(image)
            image = np.expand_dims(image, axis=0)
            data: np.ndarray
            for image in resize_images(images_array=image, image_format='rgb'):
                np.append(data, image)
            data = np.expand_dims(data, axis=0)

            model_loaded = keras.saving.load_model("./recognizerapp/model")
            predicted = model_loaded.predict(data).tolist()
            maxi = predicted.index(max(predicted))
            emotion = emotions[maxi]
            context['image'] = image
            context['emotion'] = emotion
            results = {'image': img_res, 'emotion': emotion, 'user': user}
            Results.objects.create(**results)
    else:
        form = NeuralNetworkForm()
    context['form'] = form
    return render(request, 'recognizerapp/NNform.html', context=context)


class ResultsCreateView(CreateAPIView):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

    def perform_create(self, serializer):
        image_data = self.request.data.get('image')
        image_serializer = ImagesSerializer(data=image_data)
        if image_serializer.is_valid():
            image = image_serializer.save()
            serializer.save(image=image)   # Создает объекты моделей Images и Results в соответствии с моделями

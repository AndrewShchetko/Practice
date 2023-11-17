from PIL import Image
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
            for image in resize_images(images_array=image):
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


class UseNNAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        form = NeuralNetworkForm(request.data, request.FILES)
        print("form.isnt_valid")
        if form.is_valid():
            print("form.is_valid")
            img_res = form.save()
            # print(ImagesSerializer(request, data=img_res).is_valid())
            # print(f'data ----  {form.cleaned_data}')
            # if ImagesSerializer(request, data=img_res).is_valid():
            #     print("is valid")
            #     serialized_img = ImagesSerializer(request, data=img_res).save()
            # else:
            #     return Response({'detail': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)
            
            cleaned = form.cleaned_data
            img = cleaned['image']
            print('HEAR')

            image = Image.open(img).convert('L')
            image = np.asarray(image)
            image = np.expand_dims(image, axis=0)
            data: np.ndarray = np.empty(image.shape)
            for image in resize_images(images_array=image):
                data = np.append(data, np.expand_dims(image, axis=0), axis=0)
                print(data.shape)

            model_loaded = keras.saving.load_model("./recognizerapp/model")
            predicted = model_loaded.predict(data).tolist()
            maxi = predicted.index(max(predicted))
            emotion = emotions[maxi]
            print(f"emotion --- {emotion}")

            results = {'image': img_res, 'emotion': emotion, 'user': user}
            Results.objects.create(**results)

            serializer = ResultsSerializer(data=results)
            if serializer.is_valid():
                serializer.save(image=serialized_img)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = request.user
        context = {'user': user}
        form = NeuralNetworkForm()
        context['form'] = form
        return render(request, 'recognizerapp/NNform.html', context=context)
# Создает объекты моделей Images и Results в соответствии с моделями

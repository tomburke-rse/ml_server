import json
import uuid
from random import randint
from time import sleep

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
from PIL import Image
from numpy import asarray
import io
import matplotlib.pyplot as plt


@api_view(['GET'])
def index(request):
    context = {
        'a': "text",
        'b': 1,
        'c': 2.0,
        'b': True,
    }
    return render(request, 'index.html', context=context)


@api_view(['POST'])
def post(request):
    # use request information
    from pathlib import Path
    Path("mysite/media").mkdir(parents=True, exist_ok=True)
    image = Image.open(request.data['img'])
    filename = "media/" + str(uuid.uuid1()) + ".png"
    image.save("mysite/"+filename, "PNG")
    print(filename)
    # do ML here, lets sleep for now
    # sleep(randint(1, 10))

    # respond with the result of ML

    response = HttpResponse(json.dumps({"result": filename}), status=status.HTTP_200_OK)
    return response

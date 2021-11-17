from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .forms import *
from .models import *
from .predict import prediction
from django.contrib import messages
import os
# Create your views here.

def home(request):
    return render(request,'home.html')


def take_img(request):

    if request.method == "POST" and 'upload_btn' in request.POST:

        form=upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=upload_form()
    if request.method == "POST" and 'check_btn' in request.POST:
        obj=upload_img.objects.all().last()

        img_path= obj.image_upload

        #x=str(img_path)
        #x=x.replace('/','\')

        #updated_path=img_path.replace(r",'\\')
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(img_path)
        #print("***************************")
        #print(x)

        get_class=prediction(str(img_path))

        print("#####################")
        print(get_class)

        return render(request, 'result.html', {"uploaded_image": obj, "result": get_class})

    return  render(request,'index.html')
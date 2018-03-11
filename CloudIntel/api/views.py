from django.shortcuts import render
from .forms import APICallForm
import numpy as np
from CloudIntel.libs.load_pickle import LoadModel
import json
from CloudIntel.libs.callback_saver import CallBackSaver
from CloudIntel.libs.dynamic_lib_loader import lib_loader


# Create your views here.
def API_UI(request):
    textcont ="""
def  test(self, result):
    if result[0]==0:
        name = 'Iris Setosa'
    elif result[0]==1: 
        name = 'Iris Versicolour '
    else result[0]==2:
        name = 'Iris Virginica'
    
    return {"name":name,"outcome":result[0]}
    """


    return render(request,"api/apifrontend.html",{"textcontent":textcont})


def API_Call(request):

    if request.method == 'GET':
        form = APICallForm(request.GET)
        if form.is_valid():
            data = []
            param1= form.cleaned_data.get('param1')
            param2= form.cleaned_data.get('param2')
            param3= form.cleaned_data.get('param3')
            param4= form.cleaned_data.get('param4')

            data.append(param1)
            data.append(param2)
            data.append(param3)
            data.append(param4)

            nparray = np.array([data])

            clf = LoadModel("classifier.pkl")

            result = clf.model.predict(nparray)
            result = result.tolist()
            response = json.dumps(result)

            return render(request,'api/apiresponse.html', {"data": response})


def API_Call_With_Callback(request):
    
    if request.method == 'GET':
        form = APICallForm(request.GET)
        if form.is_valid():
            data = []
            param1= form.cleaned_data.get('param1')
            param2= form.cleaned_data.get('param2')
            param3= form.cleaned_data.get('param3')
            param4= form.cleaned_data.get('param4')

            data.append(param1)
            data.append(param2)
            data.append(param3)
            data.append(param4)

            nparray = np.array([data])

            clf = LoadModel("classifier.pkl")

            result = clf.model.predict(nparray)
            result = result.tolist()

            lib = lib_loader("CloudIntel.callback_repo.test","sample")
            lib= lib.get_class_object
            obj=lib()
            result = obj.testmethod(result)

            response = json.dumps(result)

            return render(request,'api/apiresponse.html', {"data": response})

    return render(request, 'api/apiresponse.html',{"data":"sample"})


def Save_callback():
    pass


def Without_Callback(request):
    print(request.GET)

    return render(request, 'api/apiresponse.html',{"data":"hello"})

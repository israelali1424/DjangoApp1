from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    #return(HttpResponse("Hello World"))
    my_dict = {'insert_me':"Hello I am coming from the  views.py file using django"}
    return render(request,'frist_app/index.html',context=my_dict)

# Create your views here.

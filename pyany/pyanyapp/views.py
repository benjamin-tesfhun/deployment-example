from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{'key':'go to other page'})

def other(request):
    return render(request,'other.html',{'key':'thank you for visiting our site'})
from django.shortcuts import render

# Create your views here.
def dreamboys(request):
    return render(request,'magesh.html')

def loverboys(request):
    return render(request,'muni.html')

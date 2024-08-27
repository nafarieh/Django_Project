from django.shortcuts import render

# Create your views here.
def home1(request):
    return render(request, 'index.html')

def myhome(request):
    return render(request, 'about.html')

def myhome2(request):
    return render(request, 'blog-home.html')

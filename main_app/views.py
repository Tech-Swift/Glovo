from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def about (request):
 return request, 'about.html'


def contact(request):
    return request, 'contact.html'
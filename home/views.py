from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request, 'home/about.html')

def gallery(request):
	return render(request, 'home/gallery.html')

def contact(request):
	return render(request, 'home/contact.html')
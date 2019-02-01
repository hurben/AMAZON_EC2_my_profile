from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def main(request):
	return render(request, 'index.html')
def playground(request):
	return render(request, 'playground.html')

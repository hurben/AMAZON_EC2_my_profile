from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def main(request):
	return render(request, 'index.html')
	#return render(request, 'main.html')

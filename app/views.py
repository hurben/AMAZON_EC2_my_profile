from django.shortcuts import render
from django.http import HttpResponse, Http404

import json

# Create your views here.
def main(request):
	return render(request, 'index.html')

def playground(request):

	json_file = open('/var/www/html/static/playground/user_data2.json')
	json_data = json.load(json_file)
	json_data_string = json.dumps(json_data)

	json_file.close()

	return render(request, 'playground.html', {'json_file' : json_data_string})

def test(request):
	return render(request, 'pichart_exam.html')

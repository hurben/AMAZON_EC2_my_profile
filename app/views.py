from django.shortcuts import render
from django.http import HttpResponse, Http404

import json

#other functions
def dump_json_to_string(json_data_dir):

	json_file = open(json_data_dir)
	json_data = json.load(json_file)
	json_data_string = json.dumps(json_data)
	json_file.close()

	return json_data_string


# Create your views here.
def main(request):
	return render(request, 'index.html')

def playground(request):

	if request.method == 'POST':
		print 'POST'

		network_style = request.POST.get('network_style')

		if network_style == 'input_network':
			json_data_string = dump_json_to_string('/var/www/html/static/playground/user_data2.json')
			flag = 1

		if network_style == 'default_network':
			json_data_string = dump_json_to_string('/var/www/html/static/playground/user_data.json')
			flag = 0

		return render(request, 'playground.html', {'json_file' : json_data_string, 'flag': flag})

	else:
		print 'else'
		json_data_string = dump_json_to_string('/var/www/html/static/playground/user_data.json')

		return render(request, 'playground.html', {'json_file' : json_data_string, 'flag':0})


#def show_json_network(request):
#	if request.method == 'POST':
#		json_file = open('/var/www/html/static/playground/user_data2.json')
#		json_data = json.load(json_file)
#		json_data_string = json.dumps(json_data)
#		json_file.close()
#		return render(request, 'playground.html', {'json_file' : json_data_string, 'flag':1})
#	else:
#		print 'Error in : show_json_network'


def test(request):
	return render(request, 'pichart_exam.html')

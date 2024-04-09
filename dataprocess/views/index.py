from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from dataprocess.utils.main import *
from django.shortcuts import render

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):

        if 'input-file' in request.FILES:
            myfile = request.FILES['input-file']
            if myfile.name.endswith('.txt'):
                info = main(myfile)
                return render(request, 'index.html', {'extracted_info': info})
            else:
                return render(request, 'index.html', {'error_message': 'El archivo no es un archivo de texto.'})
        else:
            return render(request, 'index.html', {'error_message': 'No se envió ningún archivo.'})

from django.shortcuts import render

def calculadora_view(request):
    return render(request, 'mi_app/index.html')
 
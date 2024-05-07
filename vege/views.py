from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def receipes(request):
    if request.method == "POST":
       data = request.POST 

       Receipe_name = data.get('Receipe_name')
       Receipe_description = data.get('Receipe_description')
       Receipe_image = request.FILES.get('Receipe_image')
       print(Receipe_name)
       print(Receipe_description)
       print(Receipe_image)


       Receipe.objects.create(
         Receipe_name=Receipe_name,
         Receipe_description=Receipe_description,
         Receipe_image=Receipe_image)
       

       return redirect('/receipe/')
    

    queryset = Receipe.objects.all()
    

    if request.GET.get('search'):
        queryset = queryset.filter(Receipe_name__icontains = request.GET.get('search'))
        # print(request.GET.get('search'))


    context = {'receipes': queryset}
    return render(request, 'receipe.html', context)


def update_receipe(request, id):
        
    queryset = Receipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST

        Receipe_name = data.get('Receipe_name')
        Receipe_description = data.get('Receipe_description')
        Receipe_image = request.FILES.get('Receipe_image')

        queryset.Receipe_name = Receipe_name
        queryset.Receipe_description = Receipe_description
        
        if Receipe_image:
            queryset.Receipe_image = Receipe_image

        queryset.save()
        return redirect('/receipe/')

    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')

def login_page(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
    

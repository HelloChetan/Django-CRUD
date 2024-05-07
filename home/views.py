from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    peoples = [
        {'name' : 'chetan', 'age' : 20},
        {'name' : 'rohan', 'age' : 19},
        {'name' : 'kamesh', 'age' : 21},
        {'name' : 'darshit', 'age' : 2},
        {'name' : 'nilesh', 'age' : 20},
        {'name' : 'nayan', 'age' : 16}
    ]
    vegetables = ['pumpkin', 'potato', 'tomato']
    for people in peoples:
        print(people)
        
    return render(request, "index.html", context = {'page': 'Heyy!!','peoples': peoples, 'vegetables': vegetables} )

def success_page(request):
    return HttpResponse("<h1>Success page bhiduu!!!</h1>")

def about_page(request):
#   return HttpResponse("<h1>This is about page</h1>")
  context = {'page':'About'}
  return render(request, "about.html", context)

def contact_page(request):
    # return HttpResponse("<h1>This is contact page</h1>")
    context = {'page': 'Contact Us'}
    return render(request, "contact.html",context)
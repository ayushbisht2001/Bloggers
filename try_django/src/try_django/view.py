from django.http import HttpResponse
from django.shortcuts import   render

def home_page(request):
    my_title = "hello frands"
    return render(request,"hello.html",{"title":my_title})

def contact_page(request):
    return HttpResponse("<h1><mark><s>contact us</mark></h2>",{"title" : "Contact us"})
def login_page(request):
    return HttpResponse("<h1><mark><s>login here</mark></h2>",{"title" : "login here"})

def about_page(request):
    return render(request,"aboutus.html",{"title":"About"})
from django.shortcuts import render

def index(request):
   
    return render(request, "index.html")

def faq(request):
    return render(request, "faq.html")

def info1(request):
    return render(request, "info1.html")

def info2(request):
    return render(request, "info2.html")

def info3(request):
    return render(request, "info3.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def htcsa(request):
    return render(request, "howto-create-steam-account.html")
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def exhibitions(request):
    return render(request, 'exhibitions.html')

def gallery(request):
    return render(request, 'gallery.html')

def porfolio(request):
    return render(request, 'porfolio.html')
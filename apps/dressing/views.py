from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dressing/index.html')

def choose_article(request):
    pass
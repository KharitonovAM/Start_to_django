from django.shortcuts import render

# Create your views here.

def main(request):
    render(request, 'main.html')

def contact(request):
    render(request,'contacts.html')
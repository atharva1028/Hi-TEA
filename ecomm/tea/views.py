from django.shortcuts import render
from .models import Person
from .models import Product
# Create your views here.
def home(request):
    item = Product.objects.all()
    return render(request,'home.html',{'item':item})
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')

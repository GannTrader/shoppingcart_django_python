from django.shortcuts import render
from django.http import HttpResponse
from .models import products
# Create your views here.
def index(request):
	listpro = products.objects.all()
	return render(request, 'home/listproducts.html', {'listpro':listpro})

def detail(request, id):
	product = products.objects.get(id=id)
	return render(request, 'home/productsdetail.html', {'pro':product})

def shoppingcart(request):
	idsp = request.POST['idsp']
	proId = products.objects.get(id=idsp)
	number = request.POST['number']
	return render(request, 'home/shoppingcart.html', {'proId':proId, 'number':number})

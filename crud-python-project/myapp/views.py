# myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer

# Frontend views
def product_list(request):
    products = Product.objects.all()
    
    print(f"Name: {products[0].name}, Price: {products[0].price}, Description: {products[0].description}")

    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        print(f"Initial Product Description: {product.description}")
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

# API views
@api_view(['GET'])
def api_product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def api_product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def api_product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return Response(status=204)

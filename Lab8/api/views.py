from itertools import product

from django.http import JsonResponse
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    data = [{ 'name':p.name,
              'id': p.id,
              'price': p.price,
              'description': p.description,
              'count': p.count,
              'is_active': p.is_active,
              'category_id': p.category_id,

    } for p in products
    ]

    return JsonResponse(data, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    data ={
        'name': product.name,
        'id': product.id,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category_id,

    }
    return JsonResponse(data, safe=False)

def category_list(request):
    categories = Category.objects.all()
    data = [{
        'name' : categories.name,
        'id' : categories.id,
    }
    for category in categories
    ]
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    data ={'name': category.name,
           'id': category.id,}
    return JsonResponse(data, safe=False)

def category_product(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    products = Product.objects.filter(category=category_id)
    data = [{
        'name': product.name,
        'id': product.id,
        'price': product.price,
        'description': product.description,
        'count': product.count

    } for product in products]
    return JsonResponse(data, safe=False)

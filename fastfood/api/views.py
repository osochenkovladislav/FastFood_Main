from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import *


@csrf_exempt
def price_api(request, ct_id=0):
    if request.method == 'GET':
        if ct_id != 0:
            price = Product.objects.filter(category=ct_id)
            price_serializer = ProductSerializer(price, many=True)
            return JsonResponse(price_serializer.data, safe=False)
        else:
            price = Product.objects.all()
            price_serializer = ProductSerializer(price, many=True)
            return JsonResponse(price_serializer.data, safe=False)


@csrf_exempt
def order_api(request, us_id=0):
    if request.method == 'GET':
        if us_id != 0:
            order = Order.objects.filter(user=us_id)
            order_serializer = OrderSerializer(order, many=True)
            return JsonResponse(order_serializer.data, safe=False)
        else:
            order = Order.objects.all()
            order_serializer = OrderSerializer(order, many=True)
            return JsonResponse(order_serializer.data, safe=False)


@csrf_exempt
def product_api(request, pr_id=0):
    if request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse('Product has been Added successfully!', safe=False)
        return JsonResponse('Failed to Add the Product!', safe=False)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(id=pr_id)
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse('Product has been Uploaded successfully!', safe=False)
        return JsonResponse('Failed to Upload the Product!', safe=False)

    elif request.method == 'DELETE':
        product = Product.objects.get(id=pr_id)
        product.delete()
        return JsonResponse('Product has been Deleted successfully!', safe=False)


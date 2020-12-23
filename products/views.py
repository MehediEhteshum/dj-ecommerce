from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from .models import Product

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html")


def products_list_view(request, *args, **kwargs):
    # return HttpResponse(Product.objects.all())
    try:
        qs = Product.objects.all()  # all products
        context = {"products": qs}
    except Product.DoesNotExist:
        raise Http404
    return render(request, "products/all.html", context)


def product_detail_view(request, pk, *args, **kwargs):
    try:
        p = Product.objects.get(pk=pk)
        context = {"product": p}
    except Product.DoesNotExist:
        raise Http404
    # return HttpResponse(f"Product id: {p.pk}, Product title: {p.title}")
    return render(request, "products/details.html", context)


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        p = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})
    return JsonResponse({
        "id": p.pk,
        "title": p.title,
        "description": p.desc,
        "price": p.price
    })

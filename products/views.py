from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, Http404

from .models import Product
from .forms import ProductModelForm

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


# def bad_view(request, *args, **kwargs):
#     # for test purpose, will not be used
#     data = dict(request.GET)
#     Product.objects.create(**data)
#     return HttpResponse(f"New product created: {str(dict(request.GET))}")

# def product_create_view(request, *args, **kwargs):
#     data = "Nothing"
#     if request.method == "POST":
#         post_data = request.POST or None
#         product_form = ProductForm(post_data)
#         form_is_valid = product_form.is_valid()
#         # False if class_variable!=form_name or ""
#         if form_is_valid:
#             data = product_form.cleaned_data.get("title")
#     context = {"data": data}
#     return render(request, "products/form_create.html", context)

@staff_member_required
def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        # though 'form' instance was made such that "" will not go through i.e. always valid
        # data = form.cleaned_data
        # Product.objects.create(**data)
        # not saved in db yet due to commit=False
        obj = form.save(commit=False)
        # do some stuff e.g. obj.user = request.user, then save
        obj.user = request.user
        obj.save()
        form = ProductModelForm()  # refreshing form after product creation
    context = {"form": form}
    return render(request, "products/form_create.html", context)


@login_required
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

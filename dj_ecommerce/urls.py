"""dj_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from accounts.views import (
    signup_view,
    login_view,
    logout_view
)

from products.views import (
    home_view,
    products_list_view,
    product_detail_view,
    # bad_view, # test purpose
    product_create_view,
    product_api_detail_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('products/', products_list_view),
    path('products/<int:pk>/', product_detail_view),
    # path('bad/', bad_view), # test purpose
    path('add-product/', product_create_view),
    # path('api/products/<int:pk>/', product_api_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view),
]

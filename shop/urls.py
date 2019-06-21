# -*- coding:utf-8 -*-
# author:aoaoc
# datetime:5/18/2019 2:02 AM
# software: PyCharm

from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
]

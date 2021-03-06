# coding:utf-8

from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import ProductAddToCartForm

def index(request, template_name):
    page_title = "产品分类目录-小白购"
    request.session['name']='hello'
    return render(request, template_name, locals())

def show_category(request, category_slug, template_name):
    c = get_object_or_404(Category, slug=category_slug)
    product = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.description
    return render(request, template_name, locals())

def show_product(request, product_slug, template_name):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    form = ProductAddToCartForm()
    return render(request, template_name, locals())







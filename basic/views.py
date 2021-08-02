from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Category, Product


def index(request):
    category = Category.objects.all()
    product = Product.objects.all().order_by('-created_at')[:8]
    product_picked = Product.objects.all().order_by('?')[:8]
    context = {
        'category': category,
        'product': product,
        'product_picked': product_picked,
    }
    return render(request, 'content.html', context)


def category_product(request, slug):
    category = Category.objects.filter(slug=slug)
    product = Product.objects.filter(category__slug=slug)
    p = Paginator(product, 2)
    page_number = request.GET.get('page')
    try:
        page = p.page(page_number)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(1)
    context = {
        'category': category,
        'product': page,
    }
    return render(request, 'category_product.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    product_latest = Product.objects.all().order_by('-created_at')[:4]
    category = Category.objects.all()
    return render(request, 'product_detail.html',
                  {'product': product, 'product_latest': product_latest, 'category': category})

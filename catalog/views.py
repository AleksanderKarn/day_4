from django.shortcuts import render

from catalog.models import Product




def home(request):
    context = {
        'object_list': Product.objects.all(),
        'template_name': 'product_list.html',
        'all_name': 'index.html',
        'header': 'header.html',
        'footer': 'footer.html'
    }
    return render(request, 'home_page.html',context)


def contacts(request):
    context = {
        'object_list': Product.objects.all(),
        'template_name': 'product_list.html',
        'all_name': 'index.html',
        'header': 'header.html',
        'footer': 'footer.html'
    }
    return render(request, 'contacts_page.html',context)


def products(request,):
    context = {
        'object_list': Product.objects.all(),
        'template_name': 'product_list.html',
        'all_name': 'index.html',
        'header': 'header.html',
        'footer': 'footer.html'
    }
    print(Product.objects.get(id=1))
    return render(request, 'index.html', context)


def product(request, id):
    context = {
        'o': Product.objects.get(id=id),
        'template_name': 'prod_info.html',
        'header': 'header.html',
        'footer': 'footer.html'


    }
    print(context)
    return render(request, 'index.html', context)
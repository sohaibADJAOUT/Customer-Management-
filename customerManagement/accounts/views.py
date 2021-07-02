from django.shortcuts import render
# from django.http import HttpResponse

# -- render : executer les templates --


def index(request):
    return render(request, "accounts/dashboard.html")


def product(request):
    return render(request, "accounts/product.html")


def customer(request):
    return render(request, "accounts/customer.html")

# -- HttpResponse : pour executer les fonctions locals --
# def product(request):
#     return HttpResponse("<h1>Hello, Product page.</h1>")


# def customer(request):
#     return HttpResponse("<b><em>Customer page.</em></b>")

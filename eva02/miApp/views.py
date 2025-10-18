from django.shortcuts import render, get_object_or_404
from .models import Producto


# Create your views here.
def main(request):
    productos = Producto.objects.all()
    return render(request, 'main.html', {'productos': productos})


def detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle.html', {'producto': producto})


def categoria(request, categoria):
    # Case-insensitive exact match so URLs like /categoria/Mundo%20Abierto/ work
    productos = Producto.objects.filter(Categoria__iexact=categoria)
    return render(request, 'categoria.html', {'productos': productos, 'categoria': categoria})
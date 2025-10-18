from .models import Producto

def categorias_context(request):
    categorias = Producto.objects.values_list('Categoria', flat=True).distinct()
    return {'categorias': categorias}
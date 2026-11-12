
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from catalogo.models import Libro, Categoria
from catalogo.forms.libro_form import LibroForm
from django.contrib.auth.decorators import login_required

@login_required
def libro_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria_id', '').strip()
    libros = Libro.objects.select_related('categoria').all()
    if pista:
        libros = libros.filter(
            Q(titulo__icontains=pista) |
            Q(autor__icontains=pista)  |
            Q(categoria__nombre__icontains=pista)
        )
    if categoria_id:
        libros = libros.filter(categoria_id=categoria_id)
        categoria_id = Categoria.objects.all()

    context = {
        'libros': libros,
        'categoria_id': categoria_id,
        'pista': pista,
        'categorias': categoria_id,
    }
    return render(request, 'catalogo/libros/libro_list.html',
                  {'libros':libros},
                   context)

def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado correctamente.')
            return redirect('libro_list')
    else:
        form = LibroForm()

    return render(
        request,
        'catalogo/libros/formulario.html',
        {'formulario': form}
    )


def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)

        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado correctamente.')
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)

    return render(
        request,
        'catalogo/libros/formulario.html',
        {'formulario': form}
    )


def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado correctamente.')
        return redirect('libro_list')

    return render(
        request,
        'catalogo/libros/confirm_delete.html',
        {'libro': libro}
    )


from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from catalogo.models import Libro
from catalogo.forms.libro_form import LibroForm


def libro_list(request):
    libros = Libro.objects.all()

    return render(
        request,
        'catalogo/libros/libro_list.html',
        {'libros': libros}
    )


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

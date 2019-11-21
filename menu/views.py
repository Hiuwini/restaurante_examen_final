from .forms import MenuForm
from .models import Menu, Venta, Plato
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


def new_menu(request):
    if request.method == "POST":
        formulario = MenuForm(request.POST)
        if formulario.is_valid():
            menu = Menu.objects.create(name=formulario.cleaned_data['name'], description = formulario.cleaned_data['description'], total = formulario.cleaned_data['total'])
            for plato_id in request.POST.getlist('platos'):
                venta = Venta(plato_id=plato_id, menu_id = menu.id)
                venta.save()
            messages.add_message(request, messages.SUCCESS, 'Se Guardado Correctamente!')
    else:
        formulario = MenuForm()
    return render(request, 'restaurante/menu_editar.html', {'formulario': formulario})

def platos(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'restaurante/post_detail.html', {'menu': menu})

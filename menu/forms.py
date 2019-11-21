from django import forms

from .models import Plato, Menu


class MenuForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Menu
        fields = ('name', 'description', 'total' ,'platos')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
def __init__ (self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields["platos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["platos"].help_text = "Platillos del Menu"
        self.fields["platos"].queryset = Plato.objects.all()

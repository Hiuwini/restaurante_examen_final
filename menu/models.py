from django.db import models
from django.contrib import admin

class Plato(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    total = models.IntegerField()
    platos = models.ManyToManyField(Plato, through='Venta')

    def __str__(self):
        return self.name

class Venta (models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class VentaInLine(admin.TabularInline):
    model = Venta
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (VentaInLine,)

class MenuAdmin (admin.ModelAdmin):
    inlines = (VentaInLine,)

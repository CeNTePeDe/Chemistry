from django.contrib import admin
from .models import Elements, Configuration, Characteristics, Period



@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'simbol', 'user')
    list_filter = ('name',)


admin.site.register(Configuration)
admin.site.register(Characteristics)
admin.site.register(Period)

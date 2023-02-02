from django.contrib import admin
from .models import Elements, Configuration, Characteristics, Period


admin.site.register(Elements)
admin.site.register(Configuration)
admin.site.register(Characteristics)
admin.site.register(Period)

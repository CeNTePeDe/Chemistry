from django.contrib import admin

from articles.models import Rubric, Key_word, Articles

admin.site.register(Rubric)
admin.site.register(Key_word)
admin.site.register(Articles)
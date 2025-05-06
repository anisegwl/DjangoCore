from django.contrib import admin
from .models import Question, Choice , Author , Publisher , Book

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
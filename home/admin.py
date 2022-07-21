from django.contrib import admin

# Register your models here.
from .models import CommentAparteman,CommentVilla

admin.site.register(CommentAparteman)
admin.site.register(CommentVilla)
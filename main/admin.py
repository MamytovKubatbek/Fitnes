from django.contrib import admin
from main.models import Form
# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'email', 'address', 'messages')

admin.site.register(Form, FormAdmin)
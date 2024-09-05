from django.contrib import admin
from .models import ClientInfo

@admin.register(ClientInfo)
class ClientInfoadmin(admin.ModelAdmin):
    list_display = ('name', 'email_add', 'contact_choice')

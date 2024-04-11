from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin', 'valid', 'status')
    # Sie können auch andere Eigenschaften wie list_filter, search_fields etc. hinzufügen

# Registrieren Sie Ihr Modell mit der benutzerdefinierten Admin-Klasse
admin.site.register(CustomUser, CustomUserAdmin)
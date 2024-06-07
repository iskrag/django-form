from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    # variable names must not be changed
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('first_name', )
    readonly_fields = ('occupation', )


# to register database and admin forms with the admin interface
admin.site.register(Form, FormAdmin)


from django.contrib import admin
from sky_settings.models import Setting


## use client-admin if present 
_modeladmin_class = admin.ModelAdmin
try:
    from client_admin.admin import ClientModelAdmin
    _modeladmin_class = ClientModelAdmin

    from client_admin.admin import TabularInline, StackedInline, GroupedInline
except ImportError as e:
    from django.contrib.admin import TabularInline, StackedInline




class SettingAdmin(_modeladmin_class):
    list_display = ('name','setting_type','value','description')
    search_fields = ('name','value')
    fieldsets = (
        (None, {'fields':('setting_type','name','value')}),
    )
admin.site.register(Setting, SettingAdmin)

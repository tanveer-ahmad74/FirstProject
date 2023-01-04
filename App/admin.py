from django.contrib import admin

from App.models import Colors
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()


class ColorModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != 'id']
        super(ColorModelAdmin, self).__init__(model, admin_site)


admin.site.register(Colors, ColorModelAdmin)
admin.site.register(User)

from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'is_superuser',)
    list_editable = ('role', 'is_superuser',)


admin.site.register(User, UserAdmin)

from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role',)
    list_editable = ('role',)


admin.site.register(User, UserAdmin)

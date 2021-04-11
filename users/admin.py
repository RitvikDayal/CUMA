from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    model = User

    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'is_superuser')

    ordering = ('-created_on',)
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Personal', {'fields': ('about', 'created_on',)}),
    )

    formfield_overrides = {
        User.about: {'widget': Textarea(attrs={'rows': 10, 'cols':40})}
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )

admin.site.register(User, UserAdminConfig)
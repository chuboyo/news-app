from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserChangeForm, UserCreationForm

class CustomUserAdmin(UserAdmin):
   add_form = UserCreationForm
   form = UserChangeForm
   model = CustomUser
   list_display = ['email', 'username', 'age', 'is_staff']
   fieldsets = UserAdmin.fieldsets + (
      (None, {'fields': ('age',)}),
   )
   add_fieldsets = UserAdmin.add_fieldsets + (
      (None, {'fields': ('age',)}),
   )

admin.site.register(CustomUser, CustomUserAdmin)
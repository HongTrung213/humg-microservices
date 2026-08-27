from django.contrib import admin
from .models import VanBanQuyChe

@admin.register(VanBanQuyChe)
class VanBanQuyCheAdmin(admin.ModelAdmin):
    list_display = ['tieu_de', 'loai', 'thu_tu', 'is_active', 'created_at']
    list_filter = ['loai', 'is_active']
    search_fields = ['tieu_de', 'noi_dung']
    prepopulated_fields = {'slug': ('tieu_de',)}

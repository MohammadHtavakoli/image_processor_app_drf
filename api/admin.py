# api/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import ProcessedImage

@admin.register(ProcessedImage)
class ProcessedImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'original_image_preview', 'processed_image_preview')
    list_filter = ('user', )
    search_fields = ('user__username',)

    def original_image_preview(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.original_image.url)
    original_image_preview.short_description = 'Original Image'

    def processed_image_preview(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.processed_image.url)
    processed_image_preview.short_description = 'Processed Image'

    readonly_fields = ('original_image_preview', 'processed_image_preview')

    fieldsets = (
        (None, {
            'fields': ('user', 'original_image', 'original_image_preview', 'processed_image', 'processed_image_preview')
        }),
    )
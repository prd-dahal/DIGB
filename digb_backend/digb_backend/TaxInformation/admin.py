from django.contrib import admin
from django.utils.safestring import mark_safe
from digb_backend.TaxInformation.models import ProgressBarModel


class ProgressBarModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    """
        This prevents any injections from html
    """
    def html_content(self, obj):
        return mark_safe(obj.content)

    html_content.short_description = 'HTML Content'


admin.site.register(ProgressBarModel, ProgressBarModelAdmin)

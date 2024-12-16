from django.contrib import admin
from .models import Portfolio, Skills, Portable
from django.urls import reverse
from django.utils.html import format_html

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'view_portfolio_link')

    def view_portfolio_link(self, obj):
        url = reverse('view_portfolio', args=[obj.id])
        return format_html('<a href="{}">View Portfolio</a>', url)

    view_portfolio_link.short_description = 'View Portfolio'

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Skills)
admin.site.register(Portable)
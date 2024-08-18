from django.contrib import admin
from .models import FootballField, FootballFieldImage


class FootballFieldImageInline(admin.TabularInline):
    model = FootballFieldImage
    extra = 1


@admin.register(FootballField)
class FootballFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact', 'price_per_hour', 'owner')
    search_fields = ('name', 'address', 'contact')
    list_filter = ('owner',)
    inlines = [FootballFieldImageInline]

    def get_queryset(self, request):
        return FootballField.all_objects.all()


@admin.register(FootballFieldImage)
class FootballFieldImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'football_field', 'image')
    search_fields = ('football_field__name',)

    def get_queryset(self, request):
        return FootballFieldImage.all_objects.all()

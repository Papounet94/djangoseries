from django.contrib import admin
from appseries.models import Serie

from datetime import timedelta, date


def next_week(modeladmin, request, queryset):
    for serie in queryset:
        serie.airing_date = serie.airing_date + timedelta(days=7)
        serie.episode += 1
        serie.save()


def end_season(modeladmin, request, queryset):
    for serie in queryset:
        serie.airing_date = date.fromisoformat("3000-01-01")
        serie.status = 'seasonend'
        serie.save()


def end_series(modeladmin, request, queryset):
    for serie in queryset:
        serie.airing_date = date.fromisoformat("4000-01-01")
        serie.status = 'terminated'
        serie.save()


next_week.short_description = 'Next Week'
end_season.short_description = 'End Season'
end_series.short_description = 'End Series'


class SerieAdmin(admin.ModelAdmin):
    actions = [next_week, end_season, end_series, ]
    list_display = ['title', 'airing_date', 'season', 'episode', 'status', ]


admin.site.register(Serie, SerieAdmin)

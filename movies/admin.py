from django.contrib import admin
from movies.models import *


class GenreInline(admin.TabularInline):
    model = Movie.genres.through
    extra = 2


class MovieCrewInline(admin.TabularInline):
    model = MovieCrew
    extra = 2


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "is_valid",)
    search_fields = ("title",)
    inlines = (MovieCrewInline, GenreInline)
    exclude = ("genres",)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("title", "is_valid",)
    search_fields = ("title",)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("title", "is_valid",)
    search_fields = ("title",)


class CrewAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender", "is_valid",)
    search_fields = ("first_name", "last_name",)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Crew, CrewAdmin)

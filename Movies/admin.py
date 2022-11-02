from django.contrib import admin

from Movies.models import *


class roleAdmin(admin.ModelAdmin):
    List_display = ("id", "titlel")


class GenreAdmin(admin.ModelAdmin):
    List_display = ("id", "titlel")
    search_field = ("title")


class crewAdmin(admin.ModelAdmin):
    List_display = ("id", "titlel")
    search_field = ("first_name", "last_name")
    list_filter = ("is_valid", )


class moviescrewInline(admin.TabularInline):
    model = moviescrew
    extra = 2


class GenreInlineAdmin(admin.StackedInline):
    model = movies.genres.through
    extra = 3 


class moviesAdmin(admin.ModelAdmin):
    List_display = ("id", "titlel")
    search_field = ("title",)
    list_filter = ("is_valid", )
    inline = (moviescrewInline, GenreInlineAdmin)
    exclude = ["Genre"]


admin.site.register(role, roleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(movies, moviesAdmin)
admin.site.register(crew, crewAdmin)
 






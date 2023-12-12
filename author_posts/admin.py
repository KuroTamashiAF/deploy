from django.contrib import admin
from .models import Author, Article, Comment


@admin.action(description='сбрысываение поля "autobiography" в 0 ')
def reset_autobiography(modeladmin, request, queryset):
    queryset.update(autobiography="")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ['birthday']
    fields = ['first_name', 'last_name', 'email', 'birthday', 'autobiography']
    readonly_fields = ['birthday']
    search_fields = ['first_name', 'last_name']
    search_help_text = 'Поиск по полю "first_name", "last_name"'
    actions = [reset_autobiography]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('heading', 'date_publication', 'author', 'number_views', 'status_publication')
    list_filter = ['date_publication']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_publication', 'author', 'article')
    list_filter = ['date_publication']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

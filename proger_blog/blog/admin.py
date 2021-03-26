from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryBookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    save_as = True

    save_on_top = True
    list_display = ('id', 'title', 'slug', 'created_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('tags',)
    readonly_fields = ('views', 'created_at', 'get_image')
    fields = ('title', 'slug', 'tags',
              'content', 'image', 'get_image',
              'views', 'created_at')

    def get_image(self, obj):
        """Возвращает картинку новости или нечего"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return '-'

    get_image.short_description = 'Фото'


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BookCategory, CategoryBookAdmin)
admin.site.register(Book, BookAdmin)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'

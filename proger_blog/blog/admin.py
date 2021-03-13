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


# class StudioAdmin(admin.ModelAdmin):
#     form = PostAdminForm


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


# class MasterAdminForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = \
#             mark_safe(
#                 """
#                 <span style="color:red; font-size:14px;">
#                     Рекомендуемый размер изображения: Ширина - 810 пикселов |
#                     Высота 1080 пикселов
#                 </span>
#                 """)


# class MasterAdmin(admin.ModelAdmin):
#     form = MasterAdminForm
#
#     class Meta:
#         model = Master
#         fields = '__all__'


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'

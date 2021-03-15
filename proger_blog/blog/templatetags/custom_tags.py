from django import template

from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('blog/popular_posts.html')
def get_popular(cnt=3):
    """
    Выводит наиболее просматриваемые посты (по умолчанию - 5)
    """
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}

#
# @register.inclusion_tag('blog/tags.html')
# def get_tags():
#     """Выводит облако тегов"""
#     tags = Tag.objects.all()
#     return {'tags': tags}

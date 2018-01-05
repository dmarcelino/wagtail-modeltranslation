# coding utf-8

from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from wagtail.wagtailcore.models import Page


@register(Page)
class PageTR(TranslationOptions):
    class Meta:
        managed = False

    fields = (
        'title',
        'slug',
        'seo_title',
        'search_description',
        'url_path',
    )

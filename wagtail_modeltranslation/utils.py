# coding: utf-8
import inspect
from django.utils.translation import trans_real
from modeltranslation import settings as mt_settings
from .contextlib import revert_to_current_language


def compare_class_tree_depth(model_class):
    """
     Function to sort a list of class objects, where subclasses
    have lower indices than their superclasses
    """

    return -len(inspect.getmro(model_class))


def import_from_string(name):
    """
    Returns a module from a string path
    """
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def languages_loop(languages=mt_settings.AVAILABLE_LANGUAGES, activate=True):
    """
    Generator to loop through languages while activating them

    Usage:
        for language in languages_loop():
            language_url[language] = obj.get_absolute_url()
    """
    with revert_to_current_language():
        for language in languages:
            if activate:
                trans_real.activate(language)
            yield language

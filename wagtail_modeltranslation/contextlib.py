from django.utils.translation.trans_real import activate
from modeltranslation.utils import get_language


class use_language:
    """
    Context manager to safely change language momentarily

    Usage:
        with use_language('en'):
            en_url = obj.get_absolute_url()
    """
    def __init__(self, lang):
        self.language = lang
        self.current_language = get_language()

    def __enter__(self):
        activate(self.language)

    def __exit__(self, exc_type, exc, exc_tb):
        activate(self.current_language)


class revert_to_current_language:
    """
    Context manager to safely change languages momentarily and return to current one

    Usage:
        with revert_to_current_language():
            activate('pt')
            pt_url = obj.get_absolute_url()
            activate('fr')
            fr_url = obj.get_absolute_url()
    """
    def __init__(self):
        self.current_language = get_language()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, exc_tb):
        activate(self.current_language)

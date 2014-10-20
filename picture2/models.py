import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path on django CMS 3.0.4+ for information
        """
        return instance.get_media_path(filename)
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class Picture2(CMSPlugin):
    """
    A Picture with or without a link.
    """

    alt = models.CharField(
        _("HTML"), max_length=255, blank=True, null=True,
        help_text=_("HTML Code"))

    def __str__(self):
        if self.alt:
            return self.alt
        return u"<empty>"

    def clean(self):
        pass

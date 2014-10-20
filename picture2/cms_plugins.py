from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import Picture2


class PicturePlugin2(CMSPluginBase):
    model = Picture2
    name = _("HTML")
    render_template = "cms/plugins/HTML.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'picture': instance,
            'placeholder': placeholder
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + u"cms/img/icons/plugins/image.png"

plugin_pool.register_plugin(PicturePlugin2)

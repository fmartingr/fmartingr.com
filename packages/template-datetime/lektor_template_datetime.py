# -*- coding: utf-8 -*-
import datetime


from lektor.pluginsystem import Plugin


class TemplateDatetimePlugin(Plugin):
    name = u'template-datetime'
    description = u'Adds the datetime package to the template context'

    def on_process_template_context(self, context, **extra):
        context['datetime'] = datetime

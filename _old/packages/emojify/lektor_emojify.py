# -*- coding: utf-8 -*-
import emoji

from lektor.pluginsystem import Plugin


class EmojifyPlugin(Plugin):
    name = "lektor-emojify"
    description = "Add emoji to your pages"

    def emojize(self, text):
        return emoji.emojize(text, language="alias")

    def on_markdown_config(self, config, **extra):
        class EmojizeMixin(object):
            def link(ren, link, title, text):
                text = self.emojize(text)
                return super(EmojizeMixin, ren).link(link, title, text)

            def table_cell(ren, content, **kwargs):
                result = super(EmojizeMixin, ren).table_cell(content, **kwargs)
                return self.emojize(result)

            def list_item(ren, text):
                result = super(EmojizeMixin, ren).list_item(text)
                return self.emojize(result)

            def paragraph(ren, text):
                result = super(EmojizeMixin, ren).paragraph(text)
                return self.emojize(result)

        config.renderer_mixins.append(EmojizeMixin)

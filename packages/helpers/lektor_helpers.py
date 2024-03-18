# -*- coding: utf-8 -*-
import datetime
import os

from lektor.pluginsystem import Plugin


class HelpersPlugin(Plugin):
    name = "helpers"
    description = "Helpers for my site"

    def on_process_template_context(self, context, **extra):
        # Add the datetime package to the template context
        context["datetime"] = datetime

        # Add a variable to the template context to check if the site is running in development mode
        context["is_dev"] = os.environ.get("LEKTOR_DEV") == "1"

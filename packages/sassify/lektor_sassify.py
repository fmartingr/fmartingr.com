import sass
from lektor.pluginsystem import Plugin
from werkzeug.utils import cached_property


class SassifyPlugin(Plugin):
    name = "Sassify"
    description = "Sassify"

    def on_before_build_all(self, builder, **extra):
        sass.compile(
            dirname=(
                self.config["sassify"]["src_path"],
                self.config["sassify"]["dest_path"],
            ),
            output_style="compressed",
        )

    @cached_property
    def config(self):
        conf = self.get_config()
        return {section: conf.section_as_dict(section) for section in conf.sections()}

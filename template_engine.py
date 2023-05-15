class TemplateEngine:
    def __init__(self):
        self.placeholder = "[DESCRIPTION]"

    def render_template(self, template, values):
        rendered_template = template.replace(self.placeholder, values)
        return rendered_template

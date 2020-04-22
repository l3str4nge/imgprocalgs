from flask import render_template



class TemplateView:
    def __init__(self, template_name, **kwargs):
        self.template_name = template_name
        self.kwargs = kwargs

    def as_view(self):
        return render_template(self.template_name, **self.kwargs)

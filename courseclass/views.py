from django.views.generic import TemplateView
from classes.models import Class

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['classes'] = Class.objects.all()
        return context
from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.


## Sending the context into FE
class TempDataRender(TemplateView):
    template_name = 'Render_context.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    ## context --> empty dictionary context object
        context['name'] = 'Tushar'
        context['age'] = 25
        context['location'] = 'Odisha'
        return context

"""
File docstring format should be determined.
"""

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


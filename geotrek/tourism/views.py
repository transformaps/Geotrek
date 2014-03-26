from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from mapentity.views import JSONResponseMixin

from geotrek.tourism.models import DataSource


class DataSourceList(JSONResponseMixin, ListView):
    model = DataSource

    def get_context_data(self):
        results = []
        for ds in self.get_queryset():
            results.append({
                'id': ds.id,
                'title': ds.title,
                'url': ds.url,
                'type': ds.type,
                'pictogram': ds.pictogram or '',
            })
        return results

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DataSourceList, self).dispatch(*args, **kwargs)

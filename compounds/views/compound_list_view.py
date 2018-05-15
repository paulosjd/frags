from django.views import generic

from compounds.models.compound import Compound


class CompoundListView(generic.ListView):
    model = Compound
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update({
        #     'object_list_lon': Site.london_sites.all(),
        #     'site_names': site_names,
        #             })
        return context

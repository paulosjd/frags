from django.shortcuts import redirect, reverse

from compounds.models import Odorant, UserOdorant
from compounds.views.odorant.odorant_list import BaseOdorantListView


class OdorantSearchFilterListView(BaseOdorantListView):

    def dispatch(self, request, *args, **kwargs):
        print(kwargs.get('search_query'))
        print(kwargs.get('search_query')[0].isnumeric)
        try:
            cas = True if kwargs.get('search_query')[0].isnumeric() and \
                          kwargs.get('search_query')[1].isnumeric() else False
            if cas:
                obj_id = Odorant.objects.get(cas_number=kwargs.get('search_query')).id
                return redirect(reverse('odorant-detail', kwargs={'pk': obj_id}))
            self.queryset = Odorant.objects.filter(
                iupac_name__contains=kwargs.get('search_query'))
            print(self.queryset)
        except (IndexError, Odorant.DoesNotExist):
            pass
        return super(OdorantSearchFilterListView, self).dispatch(request, *args, **kwargs)


class OdorantChemFilterListView(BaseOdorantListView):
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(OdorantChemFilterListView, self).get_context_data(**kwargs)
        context['chem_type'] = self.kwargs['chem_type']
        context['page_header'] = self.kwargs['chem_type'].replace('_', ' ')
        return context

    def get_queryset(self):
        unfiltered = super(OdorantChemFilterListView, self).get_queryset
        filter_method = getattr(Odorant.objects, self.kwargs['chem_type'], unfiltered)
        return filter_method()


class UserOdorantChemFilterListView(OdorantChemFilterListView):
    template_name = 'odorants/user_odorant_list.html'
    context_object_name = 'compound_list'

    def get_queryset(self):
        notes_qs = UserOdorant.objects.filter(user=self.request.user.profile).values('compound')
        if not notes_qs:
            return Odorant.objects.none()
        cpd_id_list = [a['compound'] for a in notes_qs]
        queryset = super(UserOdorantChemFilterListView, self).get_queryset().filter(id__in=cpd_id_list)
        return queryset

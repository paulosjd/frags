from django.contrib import admin

from compounds.models import Odorant, UserNotes, OdorType, Profile, Substructure
from compounds.forms.admin import SubstructureAdminForm


@admin.register(Odorant)
class OdorantAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('cas_number', 'chemical_properties', 'cid_number', 'iupac_name', 'smiles')
        return self.readonly_fields


@admin.register(UserNotes)
class CompoundNotesAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(OdorType)
class OdorAdmin(admin.ModelAdmin):
    pass


@admin.register(Substructure)
class SubstructureAdmin(admin.ModelAdmin):
    form = SubstructureAdminForm
    readonly_fields = ['iupac_name']

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import JSONField
import cirpy
import pubchempy as pcp


class CompoundMixin(models.Model):
    """ A mixin to provide fields whose values allow chemical properties to be obtained """

    chemical_properties = JSONField(
        default=dict,
        editable=False,
        blank=True,
    )
    trade_name = models.CharField(
        max_length=20,
        default='',
        verbose_name='Trade name',
        blank=True,
    )

    @property
    def structure_url(self):
        if hasattr(self, 'cid_number'):
            return 'https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={}&amp;t=l'.format(self.cid_number)

    def set_chemical_data(self, identifier, pcp_query=None):
        if not identifier or not self.chemical_properties:
            if hasattr(self, 'inchikey') and identifier == self.inchikey:
                pcp_query = pcp.get_compounds(identifier, 'inchikey')
            elif hasattr(self, 'cas_number') and identifier == self.cas_number:
                cirpy_query = cirpy.query(identifier, 'smiles')
                if not cirpy_query:
                    raise ValidationError('No compound matches the CAS number')
                self.smiles = cirpy_query[0].value
                pcp_query = pcp.get_compounds(self.smiles, 'smiles')
            if not pcp_query:
                raise ValidationError('No compound match found')
            data = {a: getattr(pcp_query[0], b) for a, b in
                    (('xlogp', 'xlogp'), ('hac', 'heavy_atom_count'), ('rbc', 'rotatable_bond_count'))}
            data.update({
                'mw': int(pcp_query[0].molecular_weight),
                'synonyms': ', '.join(pcp_query[0].synonyms[:5]),
                'hetac': len(''.join([i for i in self.smiles if i in ['O', 'N', 'S', ]]))
                         })
            self.chemical_properties = data

    class Meta:
        abstract = True
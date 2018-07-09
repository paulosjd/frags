from django.db import models
from django.core.exceptions import ValidationError
import cirpy
import pubchempy as pcp


class ChemDescriptorMixin(models.Model):
    """ A mixin to provide fields whose values allow chemical properties to be obtained """

    smiles = models.CharField(
        db_index=True,
        max_length=100,
        default='',
        verbose_name='SMILES string',
        blank=True,
    )
    iupac_name = models.CharField(
        db_index=True,
        max_length=200,
        default='',
        verbose_name='IUPAC name',
        editable=False,
        blank=True,
    )
    cid_number = models.IntegerField(
        verbose_name='PubChem API CID number',
        blank=True,
    )

    @property
    def structure_url(self):
        return 'https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={}&amp;t=l'.format(self.cid_number)

    def set_pcp_data(self):
        if not self.cid_number:
            try:
                self.cid_number = pcp.get_compounds(self.smiles, 'smiles')[0].cid
            except (IndexError, pcp.BadRequestError):
                raise ValidationError('Something went wrong B')
        if not self.iupac_name:
            self.iupac_name = cirpy.Molecule(self.smiles).iupac_name

    class Meta:
        abstract = True

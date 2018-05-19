from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.functional import cached_property
import cirpy
import pubchempy as pcp

from compounds.models.odor import Odor
from compounds.models.mixins.supplier import SupplierMixin

# TODO: make so if enter trade_name, also require supplier. And def str like if self.trade_name: return '{} ({}) {}'.format(self.trade_name, self.supplier. self.iupac_name


class Compound(SupplierMixin, models.Model):

    cas_number = models.CharField(
        max_length=20,
        verbose_name='CAS number',
        validators=[RegexValidator(r'\d+(?:-\d+)+', "String should be a valid CAS number")],
    )
    smiles = models.CharField(
        max_length=100, default='',
        verbose_name='SMILES string',
        editable=False,
    )
    iupac_name = models.CharField(
        max_length=200, default='',
        verbose_name='IUPAC name',
        editable=False,
    )
    cid_number = models.IntegerField(
        blank=True, null=True,
        verbose_name='PubChem API CID number',
        editable=False,
    )
    odor_description = models.CharField(
        max_length=500, default='',
        verbose_name='Odor description',
    )
    odor = models.ManyToManyField(
        Odor, related_name='compounds',
        verbose_name='Odor Category'
    )

    class Meta:
        ordering = ['-trade_name', 'iupac_name']

    @cached_property
    def pubchem(self):
        try:
            synonyms = ', '.join(pcp.get_compounds(self.cid_number)[0].synonyms)
        except KeyError:
            synonyms = 'n/a'
        structure_url = 'https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid={}&amp;t=l'.format(self.cid_number)
        return {'image_url': structure_url, 'synonyms': synonyms}


    def save(self, *args, **kwargs):
        if not self.smiles:
            cas_no = self.cas_number
            cirpy_query = cirpy.query(str(cas_no), 'smiles')
            try:
                self.smiles = cirpy_query[0].value
                self.cid_number = pcp.get_compounds(self.smiles, 'smiles')[0].cid
            except (IndexError, pcp.BadRequestError):
                raise ValidationError('No compound found for this CAS number')
            self.iupac_name = cirpy.Molecule(self.smiles).iupac_name
        super(Compound, self).save(*args, **kwargs)

    def __str__(self):
        if self.trade_name and self.supplier:
            return '{} ({}) | {}'.format(self.trade_name, self.supplier, self.iupac_name)
        return self.iupac_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse(
            'compound-detail',
            args=[str(self.pk)],
        )


    # TODO: method to populate empty imagefield using rdkit.MoltoImage save on local or S3 - or property decorator instead to generate on demand?
# cirpy_query = cirpy.query('126-91-0', 'smiles')
#
# cirpy_query
#
# [Result(input='126-91-0', representation='smiles', resolver='cas_number', input_format='CAS Registry Number', notation='126-91-0', value='CC(C)=CCC[C@@](C)(O)C=C')]
#
# mol.image_url
#

        #
        # structure_choices = (
        #     ('ali', 'Aliphatic'),
        #     ('atp', 'Acyclic terpence'),
        #     ('ctp', 'Cyclic terpene'),
        #     ('ocy', 'Other cycloaliphatic'),
        #     ('aro', 'Aromatic'),
        #     ('het', 'Heterocyclic'),
        # )
        # fg_choices = (
        #     ('hyd', 'Hydrocarbon'),
        #     ('alc', 'Alcohol or ether'),
        #     ('ald', 'Aldehyde or acetal'),
        #     ('ket', 'Ketone'),
        #     ('cad', 'Carboxylic acid derivative'),
        #     ('cye', 'Cyclic ether'),
        #     ('lac', 'Lactone'),
        #     ('msc', 'Miscellaneous'),
        # )
        #
# 'https://cactus.nci.nih.gov/chemical/structure/Cc1cccc%28CCCCCO%29c1/image'
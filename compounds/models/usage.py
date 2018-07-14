from django.db import models
from django.shortcuts import reverse

from compounds.models import Odorant, Profile

# cost
# notes
# rating value


class Usage(models.Model):

    types = (
        (1, 'Fragrance composition'),
    )
    type = models.IntegerField(
        choices=types,
        default=1,
    )
    name = models.CharField(
        max_length=30,
        default='untitled',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        null=True,
    )
    created_by = models.ForeignKey(
        Profile,
        related_name='usages',
    )
    # for use with type 1.
    ingredients = models.ManyToManyField(
        Odorant,
        through='Component')
    # def save(...):
        #Validate ingredients add up to 100% and such


class Component(models.Model):
    composition = models.ForeignKey(
        Usage,
        on_delete=models.CASCADE,
    )
    compound = models.ForeignKey(
        Odorant,
        on_delete=models.CASCADE,
    )
    proportion = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )



# class OdorType(models.Model):
#     term = models.CharField(
#         max_length=20,
#         unique=True
#     )
#     description = models.TextField(
#         max_length=200,
#         default=''
#     )
#
#     def __str__(self):
#         return self.term
#
#     def get_absolute_url(self):
#         return reverse(
#             'compound-odor-type-filter',
#             args=[str(self.term)],
#         )
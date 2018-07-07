from django import forms


class CompoundSearchForm(forms.Form):

    cas_number = forms.CharField(
        label='CAS number',
        max_length=12,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. 80-54-6', }),
    )
    iupac_name = forms.CharField(
        label='Compound name',
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. 2-phenylethyl', }),
    )

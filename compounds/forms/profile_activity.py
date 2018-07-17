from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from compounds.models import UserCompound, Odorant, Profile


class CompoundNotesForm(forms.ModelForm):

    """ Form for users to create a CompoundNote instance for a given Compound instance """

    user = forms.ModelChoiceField(
        queryset=Profile.objects.all(),
        widget=forms.HiddenInput(),
    )
    compound = forms.ModelChoiceField(
        queryset=Odorant.objects.all(),
        widget=forms.HiddenInput(),
    )
    notes = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 42, 'placeholder': 'Enter notes',
                   'style': 'border-color: green;', }),
    )

    class Meta:
        model = UserCompound
        fields = ['notes', 'user', 'compound']

    def __init__(self, *args, **kwargs):
        user_auth = kwargs.pop('user_auth', None)
        notes = kwargs.pop('notes', None)
        super(CompoundNotesForm, self).__init__(*args, **kwargs)
        if notes:
            self.fields['notes'].initial = notes
        if not user_auth:
            self.fields['notes'].widget.attrs['placeholder'] = 'Login to access notes'

    def save(self, **kwargs):
        try:
            UserCompound.objects.get(compound=self.cleaned_data['compound']).delete()
        except UserCompound.DoesNotExist:
            pass
        super(CompoundNotesForm, self).save(**kwargs)


class UserLiteratureRefsForm(forms.Form):
    lit_ref_numbers = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        available_choices = kwargs.pop('lit_records')
        super(UserLiteratureRefsForm, self).__init__(*args, **kwargs)
        self.fields['lit_ref_numbers'].choices = [(a, '') for a in available_choices]


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in ('username', 'email', 'password1', 'password2'):
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

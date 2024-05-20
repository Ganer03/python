from django import forms
from .models import Case, Client


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['area', 'title', 'description']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'case']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['case'].queryset = Case.objects.all()
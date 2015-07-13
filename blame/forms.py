from django import forms

PLACE_HOLDER = 'Type in any .js, .py or .mako file name in the osf'

class QueryForm(forms.Form):
    query = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': PLACE_HOLDER}),
                            )

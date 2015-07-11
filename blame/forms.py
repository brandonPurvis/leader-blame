from django import forms


class SearchForm(forms.Form):
    file_query = forms.CharField()

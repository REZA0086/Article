from django import forms


class ArticleForm(forms.Form):
    q = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': "text", 'class': "nav__search-input", 'placeholder': "جستجو مقالات"
    }))


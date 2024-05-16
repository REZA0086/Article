from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'id': "comment", 'name': "comment", 'rows': "5", 'required': "required"
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={'name': "name", 'id': "name", 'type': "text"}))

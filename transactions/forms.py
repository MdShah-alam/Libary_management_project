from django import forms
from . models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model=BookModel
        fields='__all__'

class EditForm(forms.ModelForm):
    class Meta:
        model=BookModel
        exclude=['isbn']
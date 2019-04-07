from django import forms

from .models import WishList, Book




class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['book_title']
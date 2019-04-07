from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from .models import WishList, Book

class IndexView(generic.ListView):
    template_name = 'list/index.html'

    def get_queryset(self):
        return WishList.objects.all()


class DetailView(generic.DetailView):
    model = WishList
    template_name = 'list/detail.html'

class WishListCreate(CreateView):
    model = WishList
    fields = ['wishlist_title']

class WishListDelete(DeleteView):
    model = WishList
    success_url = reverse_lazy('list:index')

def create_book(request, wishlist_id):
    form = BookForm(request.POST or None, request.FILES or None)
    wishlist = get_object_or_404(WishList, pk=wishlist_id)
    if form.is_valid():
        wishlist_books = wishlist.book_set.all()
        for b in wishlist_books:
            if b.book_title == form.cleaned_data.get("book_title"):
                context = {
                    'wishlist': wishlist,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'list/create_book.html', context)
        book = form.save(commit=False)
        book.wishlist = wishlist
        book.save()
        return render(request, 'list/detail.html', {'wishlist': wishlist})
    context = {
        'wishlist': wishlist,
        'form': form,
    }
    return render(request, 'list/create_book.html', context)

def delete_book(request, wishlist_id, book_id):
    wishlist = get_object_or_404(WishList, pk=wishlist_id)
    song = Book.objects.get(pk=book_id)
    song.delete()
    return render(request, 'list/detail.html', {'wishlist': wishlist})



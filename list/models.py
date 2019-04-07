from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

#Make sure to sync up with database after adding attributes
#python manage.py makemigrations list
#then python manage.py migrate
class WishList(models.Model):
    wishlist_title = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('list:index')

    def __str__(self):
        return self.wishlist_title

class Book(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=250)


    def __str__(self):
        return self.book_title


#wishlistname = WishList.objects.get(pk=1)
#wishlistname.book_set.all() reveals the set of books within the wishlist
#Create new books with wishlistname.book_set.create(set all attributes here)
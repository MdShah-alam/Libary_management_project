from django.db import models
from accounts.models import Account
    
class BookModel(models.Model):
    isbn = models.IntegerField(unique=True , help_text="Enter the isbn number of book.")
    amount = models.IntegerField(help_text="How many books you store.")
    book_name = models.CharField(max_length=100 , help_text="Enter your book name.")
    author = models.CharField(max_length=30 ,help_text="Enter book writter name.")
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.book_name} {self.isbn}'
    
class Categorymodel(models.Model):
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE , related_name='categoryy' , help_text="Enter the category of book.")
    categoy=models.CharField(max_length=50 , primary_key=True)
    
    def __str__(self):
        return f'{self.categoy}'
    

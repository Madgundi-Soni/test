from django.db import models
from datetime import date

# Create your models here.

class Books(models.Model):
    b_id=models.CharField(max_length=200, null=True,blank=True)
    title=models.CharField(max_length=200, null=True,blank=True)
    authors=models.CharField(max_length=200, null=True,blank=True)
    avarage_rating=models.CharField(max_length=200, null=True,blank=True)
    isbn=models.CharField(max_length=200, null=True,blank=True)
    isbn13=models.CharField(max_length=200, null=True,blank=True)
    language_code=models.CharField(max_length=200, null=True,blank=True)
    num_pages=models.IntegerField(null=True,blank=True)
    publication_date=models.CharField(max_length=200,null=True,blank=True)
    publisher=models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.title

    
class Members(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Transactions(models.Model):
    books=models.ForeignKey(Books,on_delete=models.CASCADE)
    members=models.ForeignKey(Members,on_delete=models.CASCADE)
    # members=models.CharField(max_length=200, null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True,blank=True)
    amount=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.members.name

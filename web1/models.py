from django.db import models
from datetime import datetime
# Create your models here.
class books_taken(models.Model):
	user_name = models.CharField(max_length=30)
	roll_no = models.IntegerField()
	book_id = models.IntegerField()
	book_name = models.CharField(max_length=30)
	book_author = models.CharField(max_length=30)
	taken_time = models.DateTimeField("taken_on",default=datetime.now())
	
	def __str__(self):
		return self.user_name



class books_requested(models.Model):
	book_name = models.CharField(max_length=30)
	book_author = models.CharField(max_length=30)
	book_id = models.IntegerField(primary_key=True)
	def __str__(self):
		return self.book_name
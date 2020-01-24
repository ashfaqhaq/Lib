from django.contrib import admin
from .models import books_taken,books_requested
# Register your models here.


class libAdmin(admin.ModelAdmin):
	fieldsets = [
	("user_profile",{"fields":["user_name","roll_no"]}),
	("book_details",{"fields":["book_id","book_name","book_author","taken_time"]})
	]
admin.site.register(books_taken,libAdmin)
admin.site.register(books_requested)
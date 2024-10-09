from django.db import models

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=30, null=False)
    author_name = models.CharField(max_length=30, null=False)
    publication_year = models.CharField(max_length=4, null=False)
    price = models.IntegerField(null=False)

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author_name": self.author_name,
            "publication_year": self.publication_year, 
            "price": self.price
        }


class Users(models.Model):
    User_name = models.CharField(max_length=30, null=False)
    user_id = models.AutoField(primary_key=True) 
    user_phone_no = models.CharField(max_length=10, null=False, default="")

    def user_dict(self):
        return {
            "user_id": self.user_id,
            "User_name": self.User_name,
            "user_phone_no": self.user_phone_no
        }

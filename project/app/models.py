from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_id = models.IntegerField()
    gender = models.BooleanField()
    couple = models.IntegerField()

class Review(models.Model):
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    contents = models.TextField()

class Comment(models.Model):
    review_id = models.IntegerField()
    user_id = models.IntegerField()
    contents = models.TextField()

class Item(models.Model):
    name= models.CharField(max_length=100)
    price = models.IntegerField()
    main_img = models.ImageField(upload_to='images/')
    hover_img = models.ImageField(upload_to='images/')
    detail_img1 = models.ImageField(upload_to='images/')
    detail_img2 = models.ImageField(upload_to='images/')
    detail_img3 = models.ImageField(upload_to='images/')
    gender = models.IntegerField()
    types = models.CharField(max_length=100)
    color = models.CharField(max_length=500)
    remark = models.CharField(max_length=100)
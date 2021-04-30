from django.db import models

class Contact(models.Model):
     name   = models.CharField(max_length=50)
     mobile   = models.CharField(max_length=50)
     email   = models.CharField(max_length=50)
     password   = models.CharField(max_length=50)
     followers   = models.CharField(max_length=200)
     following   = models.CharField(max_length=200)
     photo   = models.TextField()

     def __str__(self):
         return self.name

class user_post(models.Model):

     description   = models.TextField()
     filedata      = models.FileField()
     visibility    = models.CharField(max_length=200)
     userid        = models.CharField(max_length=200)

     def __str__(self):
         return self.description



class userconnection(models.Model):


     userId              = models.CharField(max_length=200)
     userConnectionId    = models.CharField(max_length=200)

     def __str__(self):
         return self.userConnectionId


class followcount(models.Model):


     followId             = models.CharField(max_length=200)
     noOfFollow          = models.IntegerField(max_length=200)

     def __str__(self):
         return self.followId

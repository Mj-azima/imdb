from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from accounts.models import MyUser


from datetime import date
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    director = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    # ba choices zade nashavad

    def __str__(self):
        return self.title




class Profile(models.Model):
    age = models.IntegerField(null=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone = models.CharField('شماره همراه', max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user




@receiver(post_save, sender=MyUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    # content_type = models.ForeignKey( on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    film = models.ForeignKey(Film,on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.film.title


class Dislike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

    film = models.ForeignKey(Film,on_delete=models.CASCADE , null=True)

    def __str__(self):
        return self.film.title


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=1028)
    film = models.ForeignKey(Film,on_delete=models.CASCADE , null=True)
    # comments = GenericRelation('Comment', null=True)

    def __str__(self):
        return self.film.title






# class Comment(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
#     text = models.CharField(max_length=1200, null=True)
#     approved = models.BooleanField(default=False)
#     create_datetime = models.DateTimeField(auto_now_add=True, null=True)
#     comments = GenericRelation('Comment')
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
#     object_id = models.PositiveIntegerField(null=True)
#     content_object = GenericForeignKey()
#
#     def __str__(self):
#         if hasattr(self.content_object, 'title'):
#             return '%s - %s' % (self.content_object.title, ' '.join(self.text.split()[:10]))
#         else:
#             return ' '.join(self.text.split()[:10])

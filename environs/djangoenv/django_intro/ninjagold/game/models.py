from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # post
    # liked_post

class Message_Post(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    user_who_liked = models.ManyToManyField(User,related_name="liked_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

class Quote(models.Model):
    quote = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, related_name="quotes",on_delete=models.CASCADE)
    fanes = models.ManyToManyField(User,related_name="favorite_quote")

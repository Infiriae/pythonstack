from django.contrib import messages
from django.shortcuts import redirect
from django.db import models
import re
import bcrypt

class MovieManager(models.Manager):
    def validate(self,postData):
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = "Title cannot be less than 2 characters"
        if len(postData['director'])<2:
            errors['director'] = "Director cannot be less than 2 characters"
        return errors


class Movie(models.Model):
    objects = MovieManager()


class UserManager(models.Manager):
    def validate(self,formData):
        errors = {}
        print(formData['email'])
        if len(formData["first_name"]) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(formData["last_name"]) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(formData["email"]) < 2:
            errors['email'] = "Email should be at least 2 characters"
        if len(formData["password"]) < 2:
            errors['password'] = "Password should be at least 2 characters"
        if formData["confirm_password"] != formData['password']:
            errors['confirm_password'] = "Password doesn't match"
        if not re.match(r"[^@]+@[^@]+\.[^@]+",formData['email']):
            errors['invalid_email'] = "Invalid Email Address"

        email_check = self.filter(email=formData['email'])
        if email_check:
            errors['email_is_use'] = "Email is in use"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = UserManager()


class Facebook_Post(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts')
    #post_comments

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
    facebook_post = models.ForeignKey(Facebook_Post, related_name='post_comments', on_delete=models.CASCADE)
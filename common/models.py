from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name


class About(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.content


class Microphone(models.Model):
    image = models.ImageField(upload_to='images/')


class Feedback(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class CallBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.email


class Info(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='images/')


class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
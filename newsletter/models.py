from django.db import models


class NewsletterSignUp(models.Model):
    email = models.EmailField(unique=True)

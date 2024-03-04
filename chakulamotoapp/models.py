from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username




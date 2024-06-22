from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    creatd_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)
    is_poblshd = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', models.PROTECT)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
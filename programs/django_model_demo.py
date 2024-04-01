from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    # one author can write multiple books 
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
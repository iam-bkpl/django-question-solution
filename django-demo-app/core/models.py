from django.db import models

class Author(models.Model):
    # public attribute 
    name = models.CharField(max_length=255)
    no_of_books_written = models.PositiveIntegerField()

    # private attribute 
    _contact = models.CharField(max_length=255)

    # protected attribute 
    _address = models.CharField(max_length=255)

    # setter method for contact
    def set_contact(self, contact):
        self._contact = contact

    # setter method for address
    def set_address(self, address):
        self._address = address

    # getter method for contact
    def get_contact(self):
        return self._contact

    # getter method for address
    def get_address(self):
        return self._address

    def __str__(self):
        return self.name
    


# # Creating author 
# python_author = Author()
# python_author.name = "Elon Musk"

# # setting author address and contact
# python_author.set_address("USA")
# python_author.set_contact("0000")


# getting author name address and contact
# author_name = python_author.name
# author_address  = python_author.get_address()
# author_contact = python_author.get_contact()



class Book(models.Model):
    title = models.CharField(max_length=255)
    # one author can write multiple books
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date = models.DateField()


    def __str__(self):
        return self.title
# Pagoda Labs

## Django Questions and Solution

**Q1: Explain the MVC pattern in the context of Django. How does it relate to the structure of a Django project?**

The MVC pattern stands for Model View And Controller.
Model: It is something that deals with database and is responsible for representing the database and performing different data related task also known as business logic.

View: It is something that deals with the user side (user-request) and is responsible for generating the UserInterface in which the user can interact and provides necessary data to the UI by getting the required data from the database.

Controller: It is something that stays between the Model and View. It is responsible for understanding the user request, calling the right View (class or method). It is basically responsible for handling different routes effectively.

Where, in case of Django we have something like (MVT) which stands for Model View Template.

Model : It is defined in models.py file. We user object oriented approach to represent the entity. and use Object Relational Mapping (ORM) to manupalate the data in the database

for eg:

```python
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
```

Here Author and Book are 2 entities that are represented using class.

View: We write views in views.py file, where, mainly we perform followings task.

1. We can define either function based views or classed views.
2. We perform ORM to the database in specific view function or method
3. We pass query data on the client side by rendering the template and passing the data as context
4. We take data from the request object and perform necessary operation

for eg:

```python
    def sayHello(request):
    context = {"name":"Kapil"}
    return render(request, "index.html", context)
```

Templates: It is the directory where we store our html files, It is the user interface through which user interacts with the system

Thus, The structure of teh django project consist of models.py, views.py and urls.py
which performs the task of models in models.py and task of views on views.py and controller in urls.py

**Q2: Write a Python program to swap the values of two variables without using a temporary variable.**

```python
    # initialization
    a = 10
    b = 20
    print("Before Swapping")

    print(f"a :{a}")
    print(f"b :{b}")

    # Swapping
    b,a = a,b

    print("After Swapping")
    print(f"a :{a}")
    print(f"b :{b}")
```

**Q3: Explain the differences between lists and tuples in Python.**

List: It is mutuble data structure in python where we can modify, the data later as per our need
for eg :

```python
books = ["DSA", "Python", "Java"]
books.append("OS")
books.remove("DSA")
```

we basically use list to store the dynamic data that might need to be updated in future.

Tuples: It is immutable data structure in python where we store such info that is not supposed to be changed in future, such as config datas.

for eg :
mytuple = (1,2,3,4)

```python
STATUS_CHOICES = (
('success', 'success'),
('failure', 'failure'),
('process', 'process'),
)
```

we basically use this to store choices in models, in django

**Q4. What is encapsulation, and how is it implemented in Python?**

Encapsulation is one of the 4 pillars of OOP. It is all about buldling the data and the methods on those data into a single unit called class. By doing so the data is hidden and only accesed through the defined methods on that class. Although the encapsulation leads to data hiding but it is not data hiding.

```python
    class Author(models.Model):
        # public attribute
        name = models.CharField(max_length=255)

        # private attribute
        __contact = models.CharField(max_length=255)

        # protected attribute
        _address = models.CharField(max_length=255)

        # setter method for contact
        def set_contact(self, contact):
            self.__contact = contact

        # setter method for address
        def set_address(self, address):
            self._address = address

        # getter method for contact
        def get_contact(self):
            return self.__contact

        # getter method for address
        def get_address(self):
            return self._address

        def __str__(self):
            return self.name

    # Creating author
    python_author = Author()
    python_author.name = "Elon Musk"

    # setting author address and contact
    python_author.set_address("USA")
    python_author.set_contact("0000")


    # getting author name address and contact
    author_name = python_author.name
    author_address  = python_author.get_address()
    author_contact = python_author.get_contact()
```

**Q5: Explain the purpose of Django's ORM (Object-Relational Mapping).**

Django ORM basically acts as the bridge between the django code and the database. It allows us to interact with the database using python objects rather than writing raw SQL queries.
for eg:

1. Allows us to interact with database using python objects and methods
2. We can use same ORM to query all types of databases. For example , to get all the books we can write : books = Book.objects.al(). This will return all the books no matter which databases we use. in short we don't need to worry about the raw sql statements to handle different databases
3. It also save our application from SQL injection attacts
4. It helps to represent the entities as an python object which makes it easier to store data and manipulate them

for example:
we can use orm to interact with the databse holding book record, such as:
all_books = Books.objects.all()
first_book = Books.objects.get(id=1)

change the name of the book
first_book.name = "first book 2.0"

delete the book
first_book.delete()

**Q6: Create a function in Python that takes a list of numbers as input and returns the sum of all even numbers in the list.**

```python
    # list initialization
    mynums = []

    user_input = input("Enter numbers and -1 when done : ")

    while user_input != "-1":
        try:
            mynums.append(int(user_input))
        except ValueError:
            print("Please enter int number")

        user_input = input()

    print("My list is :")
    print(mynums)


    # function that takes a list and check if it's even and sum all the even number in the list and returns the result
    def calc_sum(myList:list):
        sum = 0
        for i in myList:
            if i % 2 == 0:
                sum +=i

        return sum


    result = calc_sum(mynums)
    print(f"The sum of all even numbers in the list is {result}")
```

**Q7: Write a Python function that takes user input for a number and handles the exception if the input is not a valid integer.**

```python
    def get_int_number():
        try:
            num = int(input("Enter a number : "))
            print(f"You entered {num}")

        except ValueError:
            print("Please enter a number")
```

**Q8: Create a Django model representing a Book with attributes like title, author, and publication date.**

```python
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
```

**Q9: Explain the concept of decorators in Python and provide an example of a custom decorator.**

Decorators are the way of adding additional functionality to a function. They are primarly used for validating authentication, setting permissions , logging etc in django.
for example in djanog, if we have some protected views which required user to be logged in, we can use decorator called @login_required

@login_required
def protected_view(request): # protected code

Example of custom decorators :

```python
    def log_sum(func):
        def wrapper(*args, **kwargs):
            print(f"Starting sum...")
            print(f"Calling function : {func.__name__}")
            print(f"Arguments are : {args}")

            result = func(*args, **kwargs)

            print(f"The result of the function is : {result}")
            return result

        return wrapper

    @log_sum
    def sum(a,b):
        return a + b


    result = sum(3,2)
    print(f"Result : {result}")
```

**Q10: What is a generator in Python? Provide an example of a generator function.**

**Q11: Explain the Global Interpreter Lock (GIL) in Python and how it affects multithreading.**

**Q12: Discuss the key features of Django REST Framework (DRF) and how it enhances API development in Django.**

**Q13: Explain what Django Channels is and provide a use case where it is beneficial.**

**Q14: What are metaclasses in Python, and how are they different from regular classes?**

**Q15: Explain the concept of asynchronous programming in Python using the asyncio module. Provide an example.**

**Q16: What are descriptors in Python? Provide an example of how they can be used.**

**Q17: Discuss the importance of migrations in Django. How can you handle schema migrations for a database?**

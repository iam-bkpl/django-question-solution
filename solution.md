# Pagoda Labs

## Django Questions and Solution

**Q: Explain the MVC pattern in the context of Django. How does it relate to the structure of a Django project?**

    The MVC pattern stands for Model View And Controller.
    Model: It is something that deals with database and is responsible for representing the database and performing    different data related task also known as business logic.

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
    3. We pass query data on the client side by rendering the template and      passing the data as context
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

**Q: Write a Python program to swap the values of two variables without using a temporary variable.**

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

**Q: Explain the differences between lists and tuples in Python.**

Q. What is encapsulation, and how is it implemented in Python?

Q: Explain the purpose of Django's ORM (Object-Relational Mapping).

Q: Create a function in Python that takes a list of numbers as input and returns the sum of all even numbers in the list.

**Q: Write a Python function that takes user input for a number and handles the exception if the input is not a valid integer.**

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

**Q: Create a Django model representing a Book with attributes like title, author, and publication date.**

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

Q: Explain the concept of decorators in Python and provide an example of a custom decorator.

Q: What is a generator in Python? Provide an example of a generator function.

Q: Explain the Global Interpreter Lock (GIL) in Python and how it affects multithreading.

Q: Discuss the key features of Django REST Framework (DRF) and how it enhances API development in Django.

Q: Explain what Django Channels is and provide a use case where it is beneficial.

Q: What are metaclasses in Python, and how are they different from regular classes?

Q: Explain the concept of asynchronous programming in Python using the asyncio module. Provide an example.

Q: What are descriptors in Python? Provide an example of how they can be used.

Q: Discuss the importance of migrations in Django. How can you handle schema migrations for a database?

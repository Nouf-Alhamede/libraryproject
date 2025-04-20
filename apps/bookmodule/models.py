from django.db import models


class Card(models.Model):
    card_number = models.IntegerField()

    def __str__(self):
        return f"Card #{self.card_number}"

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.code})"

class Address(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    card = models.OneToOneField(Card, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

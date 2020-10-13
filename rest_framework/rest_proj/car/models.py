from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Car(models.Model):
    company = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.company


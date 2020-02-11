from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name  # позже в админке будет отображаться имя объекта, среди созданных пользователей


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    # это нужно для выподающего списка
    CATEGORY = (
        ('В помещении', 'В помещении'),
        ('На улице', 'На улице'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)  # многие ко многим

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('В ожидании', 'В ожидании'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен'),
    )
    # реалищуем отношения между несколькими базами даннных
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    # реализуем отношения между несколькими базами данных^
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name # далее это понадобится при удалении товара




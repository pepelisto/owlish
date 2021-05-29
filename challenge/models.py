from django.db import models


class City(models.Model):
    city = models.CharField(max_length=40, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.city


class Company(models.Model):
    company_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.company_name


class Title(models.Model):
    title_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.title_name


class Customer(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    gender_types = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(
        max_length=10,
        help_text='Cuenta',
        choices=gender_types
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name='companies'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name='cities'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='titles'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

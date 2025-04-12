# Setup

Create a virtual environment and install the dependencies.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Create a project

```bash
django-admin startproject carstack
cd carstack
```

# Create an app

Create a Django app:

```bash
python manage.py startapp cars
```

Add the app to the `INSTALLED_APPS` list in `carstack/settings.py`. Make sure you add `'rest_framework'`, too.

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'cars',
]
```

# Create some models

In `cars/models.py`, create some simple models:

```python
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    BODY_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('truck', 'Truck'),
        ('van', 'Van'),
    ]
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
    
    is_electric = models.BooleanField(default=False)
    color = models.CharField(max_length=50)
    mileage = models.IntegerField(default=0)
    features = models.ManyToManyField(Feature, blank=True)
    
    def __str__(self):
        return f"{self.year} {self.manufacturer.name} {self.model_name}"

```

# Create database migrations

Run the following command to create the migration files:

```bash
python manage.py makemigrations
```

Output

```bash
Migrations for 'cars':
  cars/migrations/0001_initial.py
    + Create model Feature
    + Create model Manufacturer
    + Create model Car
```

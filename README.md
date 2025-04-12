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


# Apply migrations

Then apply the migrations by running:

```bash
python manage.py migrate
```

This will create an SQLite database named `db.sqlite3` containing the tables for the models.

If you want to use another database like PostgreSQL or MySQL, update the DATABASES setting in `carstack/settings.py`.

Output


```bash
Operations to perform:
  Apply all migrations: admin, auth, cars, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying cars.0001_initial... OK
  Applying sessions.0001_initial... OK
```

# Create serializers for DRF

In `cars/serializers.py`, create serializers for the models:

```python
from rest_framework import serializers
from .models import Manufacturer, Feature, Car

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    features = FeatureSerializer(many=True)

    class Meta:
        model = Car
        fields = '__all__'
```

# Create views for DRF

In `cars/views.py`, create views for the models:

```python
from rest_framework import viewsets
from .models import Manufacturer, Feature, Car
from .serializers import ManufacturerSerializer, FeatureSerializer, CarSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
```

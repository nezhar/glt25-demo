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

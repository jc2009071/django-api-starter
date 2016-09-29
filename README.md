# Django API Starter Kit

Bare minimum to get started.

## Setup

NOTE: It is recommended to install all `pip` packages in a `virtualenv`.

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver`

Make a copy of `settings.py` from `settigns.py.init` and fill in your preferred `JWT_SECRET` and `JWT_ALGORITHM`.

## Development

A few standard processes to follow when creating new Django `Model`, `Serializer`, or `View`.

### Models

All models to be created in `models` directory for each app, and should extend `BaseModel`. This is to ensure
the fields `created_at` and `updated_at` are properly populated.

After creating the model, remember to update `__init__.py` to import the module.

Example:

```python
# api/models/__init__.py
# ...
from api.models.device import DeviceModel
# ...
```

### Serializers

All serializers are to be created with `HyperlinkedModelSerializer`, unless there is a specific reason to why it
is not used. If so, document it with the code.

### Views

Make use of Django REST Framework's `ViewSet` instead of defining own methods. If there are reasons to using normal view methods,
document it together with the code.

Similar to models, update `__init__.py` after every new view is defined.

### Routing

App specific routes are all found in the app directory's `urls.py`.

Make use of Django REST Framework's `ViewSet`.

Example:

```python
# api/urls.py
# ...
router.register(r'devices', views.DeviceViewSet)
# ...
```

### CoreAPI Support

To browse API with Core API:

**Setup**

`pip install coreapi-cli`

**Authenticate**

`coreapi credentials add 127.0.0.1 <username>:<password> --auth basic`

**Browse**

`coreapi get http://127.0.0.1:8000`

`coreapi action users list`
etc.

## TODO

- [x] Facebook and JWT Auth
- [ ] Other models implementation
- [ ] Database seeding

# Recipes app to help design a sane generic file attachments data model and workflow

Based on [this](http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/).

## Things to do

- Investigate whether this works for other models referencing the same ingredients. If not, look into the Django's [contenttypes framework](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/) and [generic relations](http://www.screamingatmyscreen.com/2012/6/django-and-generic-relations/).
- _Really_ understand how the data model works.
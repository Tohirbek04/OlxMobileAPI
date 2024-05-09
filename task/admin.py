from django.contrib import admin

from task.models import Category, Product, Valyuta

admin.site.register([Category, Product, Valyuta])

from django.db import models
from django.template.defaultfilters import slugify


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    location = models.TextField()

    def __str__(self):
        return self.first_name


class BaseModel(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(BaseModel):
    class Meta:
        verbose_name_plural = "Categories"


class Status(BaseModel):
    pass


class Valyuta(BaseModel):

    class Meta:
        verbose_name_plural = 'Valyutalar'


class Product(BaseModel):
    description = models.TextField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    see_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mobile')
    valyuta = models.ForeignKey(Valyuta, on_delete=models.CASCADE, related_name='valyuta')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status')






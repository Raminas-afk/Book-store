from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from userdata.models import UserProfile
import uuid
# Create your models here.


class Book(models.Model):
    # add image field later
    cover = models.ImageField(
        upload_to="static/covers", height_field=None, width_field=None)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    # rating = models.IntegerField(
    #     validators=[MinValueValidator(1), MaxValueValidator(5)]) Currently not needed, maybe fetch some ratings later
    description = models.TextField()
    category = models.ManyToManyField("Category")
    is_bestselling = models.BooleanField()
    quantity = models.IntegerField()
    price = models.FloatField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ID: {self.id}"


class Order(models.Model):
    order_id = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False)
    books = models.ManyToManyField(Book)
    customer = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    price = models.FloatField()
    date = models.DateField(auto_created=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id


class Cart(models.Model):
    books = models.ManyToManyField(Book)

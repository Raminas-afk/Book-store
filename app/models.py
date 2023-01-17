from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from userdata.models import UserProfile
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
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
        return self.name


class Order(models.Model):
    order_id = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False)
    books = models.ManyToManyField("Cart")
    customer = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    price = models.FloatField()
    date = models.DateField(auto_created=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id


class Cart(models.Model):
    customer = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, default=None)
    books = models.ManyToManyField(Book)
    total_price = models.FloatField()

    @receiver(post_save, sender=UserProfile)
    def create_customer_cart(sender, instance, created, **kwargs):
        if created:
            Cart.objects.create(customer=instance)

    def __str__(self):
        return f"{self.customer}'s Cart"

    def get_total_price(self):
        price = 0
        for book in self.books.all():
            price += book.price
        self.price = price
        return self.price

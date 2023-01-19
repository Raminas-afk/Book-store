# Generated by Django 4.1.5 on 2023-01-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cart_books_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(to='app.book'),
        ),
        migrations.AlterField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(to='app.book'),
        ),
    ]
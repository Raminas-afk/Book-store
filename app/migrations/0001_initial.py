# Generated by Django 4.1.5 on 2023-01-10 09:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='static/covers')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.DateField()),
                ('description', models.TextField()),
                ('is_bestselling', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('order_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('books', models.ManyToManyField(to='app.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userdata.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(to='app.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='app.category'),
        ),
    ]

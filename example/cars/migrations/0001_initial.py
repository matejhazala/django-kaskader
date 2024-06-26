# Generated by Django 4.2.3 on 2024-01-30 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'brand model',
                'verbose_name_plural': 'brand models',
                'db_table': 'example_brand_models',
                'ordering': ['brand', 'title'],
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'car brand',
                'verbose_name_plural': 'car brands',
                'db_table': 'example_car_brands',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(choices=[('DIESEL', 'Diesel'), ('GASOLINE', 'Gasoline')], max_length=8)),
                ('color', models.CharField(blank=True, choices=[('RED', 'red'), ('GREEN', 'green'), ('BLUE', 'blue'), ('WHITE', 'white'), ('BLACK', 'black'), ('YELLOW', 'yellow'), ('SILVER', 'silver'), ('PINK', 'pink')], default=None, max_length=8, null=True)),
                ('numberplate', models.CharField(max_length=16, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.brandmodel', verbose_name='car brand model')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
                'db_table': 'example_cars',
                'ordering': ['model__brand', 'model', 'numberplate'],
            },
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.carbrand', verbose_name='car brand'),
        ),
        migrations.AlterUniqueTogether(
            name='brandmodel',
            unique_together={('brand', 'title')},
        ),
    ]

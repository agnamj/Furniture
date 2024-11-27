# Generated by Django 5.1.2 on 2024-11-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0004_cart_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.TextField(blank=True, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, max_length=100, null=True)),
                ('Totalprice', models.CharField(blank=True, max_length=100, null=True)),
                ('Message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

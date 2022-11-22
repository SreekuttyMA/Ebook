# Generated by Django 4.1.3 on 2022-11-22 04:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('F', 'Fantasy'), ('L', 'Literary'), ('M', 'Mystery'), ('NF', 'Non_Fiction'), ('SF', 'Science_Fiction'), ('T', 'Thriller')], default=[('F', 'Fantasy'), ('L', 'Literary'), ('M', 'Mystery'), ('NF', 'Non_Fiction'), ('SF', 'Science_Fiction'), ('T', 'Thriller')], max_length=2)),
                ('review', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(upload_to='media/<django.db.models.fields.CharField>/'),
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0008_auto_20201002_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
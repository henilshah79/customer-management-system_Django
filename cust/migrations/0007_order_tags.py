# Generated by Django 3.1.1 on 2020-10-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='cust.Tag'),
        ),
    ]
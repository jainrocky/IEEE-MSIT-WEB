# Generated by Django 2.0.4 on 2019-03-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_auto_20190302_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execom',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]

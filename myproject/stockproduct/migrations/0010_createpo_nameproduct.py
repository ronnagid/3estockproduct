# Generated by Django 4.0.1 on 2022-01-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockproduct', '0009_alter_createpo_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='createpo',
            name='NameProduct',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

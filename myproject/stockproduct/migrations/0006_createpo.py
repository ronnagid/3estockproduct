# Generated by Django 4.0.1 on 2022-01-10 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockproduct', '0005_delete_createpo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createPo', models.CharField(max_length=100)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockproduct.stockproduct')),
            ],
        ),
    ]

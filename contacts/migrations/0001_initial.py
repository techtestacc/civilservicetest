# Generated by Django 4.2.6 on 2025-02-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(default='', max_length=152)),
                ('phoneNumber', models.IntegerField(default=0)),
            ],
        ),
    ]

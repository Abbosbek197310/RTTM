# Generated by Django 5.0.6 on 2024-07-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('yili', models.CharField(max_length=100)),
                ('malumot', models.TextField()),
                ('rasm', models.ImageField(upload_to='media/')),
                ('fayl', models.FileField(upload_to='')),
            ],
        ),
    ]

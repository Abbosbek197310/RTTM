# Generated by Django 5.0.3 on 2024-07-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_baxromjon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolim_nomi', models.CharField(max_length=200)),
                ('malumoy_nomi', models.CharField(max_length=200)),
                ('mutaxassis1', models.CharField(max_length=100)),
                ('mutaxassis2', models.CharField(max_length=200)),
                ('mutaxassis3', models.CharField(max_length=200)),
                ('mutaxassis4', models.CharField(max_length=200)),
                ('img1', models.ImageField(upload_to='media/')),
                ('img2', models.ImageField(upload_to='media/')),
                ('img3', models.ImageField(upload_to='media/')),
                ('img4', models.ImageField(upload_to='media/')),
            ],
        ),
    ]

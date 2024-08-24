# Generated by Django 5.0.3 on 2024-07-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_axborot_raxbarlar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Baxromjon',
        ),
        migrations.RenameField(
            model_name='javoxir',
            old_name='ism',
            new_name='ism3',
        ),
        migrations.RenameField(
            model_name='raxbarlar',
            old_name='ism',
            new_name='ism1',
        ),
        migrations.RenameField(
            model_name='xodimlar',
            old_name='mutaxassis1',
            new_name='ism2',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='bolim_nomi',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='malumoy_nomi',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='mutaxassis2',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='mutaxassis3',
        ),
        migrations.RemoveField(
            model_name='xodimlar',
            name='mutaxassis4',
        ),
        migrations.AddField(
            model_name='xodimlar',
            name='lavozim',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xodimlar',
            name='malumot',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

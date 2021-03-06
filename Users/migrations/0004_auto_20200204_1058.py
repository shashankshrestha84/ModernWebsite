# Generated by Django 3.0.2 on 2020-02-04 05:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usrs', '0001_initial'),
        ('Users', '0003_auto_20200203_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='RoomType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usrs.Rooms'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_merge_20200204_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomType', models.CharField(max_length=100)),
                ('Check_In', models.TextField()),
                ('Check_Out', models.TextField()),
                ('Adults', models.IntegerField(null='True')),
                ('Children', models.IntegerField(null='True')),
            ],
        ),
    ]
# Generated by Django 3.1 on 2021-08-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='images/noimage.png', upload_to='images', verbose_name='画像'),
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]

# Generated by Django 3.2.20 on 2023-07-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='camping-kampcilik-nedir.jpg', upload_to='blog/'),
        ),
    ]

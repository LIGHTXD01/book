# Generated by Django 5.1.3 on 2024-12-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_book_img_book_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.CharField(default='No text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='library',
            name='text',
            field=models.CharField(default='No text', max_length=500),
            preserve_default=False,
        ),
    ]

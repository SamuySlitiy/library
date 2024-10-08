# Generated by Django 5.1.1 on 2024-09-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['author'],
                'indexes': [models.Index(fields=['isbn'], name='library_lib_isbn_86a64d_idx')],
            },
        ),
    ]

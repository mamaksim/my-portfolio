# Generated by Django 4.2.4 on 2023-08-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]

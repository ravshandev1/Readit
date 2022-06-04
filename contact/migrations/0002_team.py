# Generated by Django 3.2.13 on 2022-06-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='team')),
                ('profession', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]

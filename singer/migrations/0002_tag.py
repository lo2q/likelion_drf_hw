# Generated by Django 5.2.4 on 2025-07-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]

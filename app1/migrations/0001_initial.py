# Generated by Django 3.1.7 on 2023-08-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=11)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
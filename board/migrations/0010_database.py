# Generated by Django 4.2.1 on 2023-06-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_alter_todo_assignedto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('color', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
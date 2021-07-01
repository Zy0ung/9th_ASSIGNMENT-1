# Generated by Django 3.2.4 on 2021-06-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_sex', models.CharField(max_length=10)),
                ('cat_img', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('cat_trait', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]

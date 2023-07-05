# Generated by Django 4.1.3 on 2023-06-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='post/')),
                ('posting_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

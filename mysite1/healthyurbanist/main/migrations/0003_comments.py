# Generated by Django 5.1.2 on 2024-11-18 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('text_comments', models.TextField(max_length=300, verbose_name='Текст комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]

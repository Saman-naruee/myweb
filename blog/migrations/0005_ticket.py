# Generated by Django 5.1.1 on 2024-11-02 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_alter_post_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='پیام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('name', models.CharField(max_length=250, verbose_name='نام')),
                ('phone', models.CharField(help_text='شماره تلفن باید 11 رقم باشد', max_length=11, validators=[django.core.validators.RegexValidator(message='شماره تلفن باید با 09 شروع شود و 11 رقم باشد.', regex='^09\\d{9}$')], verbose_name='شماره تلفن')),
            ],
        ),
    ]

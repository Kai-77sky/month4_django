# Generated by Django 4.1.1 on 2022-10-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_rename_is_acteve_client_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заказа')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата время изменения заказа')),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
            ],
        ),
    ]

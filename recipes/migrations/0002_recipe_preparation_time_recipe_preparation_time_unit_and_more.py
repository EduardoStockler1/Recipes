# Generated by Django 5.1.2 on 2025-01-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.CharField(default=43, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(default=532, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings_unit',
            field=models.CharField(max_length=12),
        ),
    ]

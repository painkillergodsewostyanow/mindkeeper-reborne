# Generated by Django 4.2 on 2023-08-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_themes_search_vector_alter_themes_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themes',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.themes'),
        ),
    ]

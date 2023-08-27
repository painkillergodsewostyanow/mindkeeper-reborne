# Generated by Django 4.2 on 2023-08-26 10:38

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


def compute_themes_search_field(apps, *args, **kwargs):
    model = apps.get_model("Themes")
    model.objects.update(search_vector=django.contrib.postgres.search.SearchVector("title"))


def compute_cards_search_field(apps, *args, **kwargs):
    model = apps.get_model("Cards")
    # TODO(before compute del html and images)
    model.objects.update(search_vector=django.contrib.postgres.search.SearchVector("title", "content"))


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('society', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36)),
                ('is_private', models.BooleanField(default=False)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.themes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society.user')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.themes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='society.user')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
            },
        ),
        migrations.AddIndex(
            model_name='themes',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='main_themes_search__ec7590_gin'),
        ),
        migrations.AddIndex(
            model_name='cards',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='main_cards_search__b32a70_gin'),
        ),
    ]

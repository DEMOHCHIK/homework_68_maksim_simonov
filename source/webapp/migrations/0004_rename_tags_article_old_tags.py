# Generated by Django 4.2.7 on 2023-12-13 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_tag_articletag_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='old_tags',
        ),
    ]
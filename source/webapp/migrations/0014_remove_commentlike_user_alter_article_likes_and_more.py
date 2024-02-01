# Generated by Django 4.2.7 on 2024-02-01 04:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0013_commentlike_articlelike_article_likes_comment_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='user',
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='article_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ArticleLike',
        ),
        migrations.DeleteModel(
            name='CommentLike',
        ),
    ]
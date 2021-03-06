# Generated by Django 4.0.2 on 2022-02-13 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('book_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_comment', to='book.book_shop')),
            ],
        ),
    ]

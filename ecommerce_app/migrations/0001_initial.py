# Generated by Django 4.0.4 on 2022-06-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publisher_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.PositiveIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.CharField(choices=[('fiction', 'Fiction'), ('literature', 'Literature'), ('stories', 'Stories'), ('historical', 'Historiacal'), ('geographical', 'geographical')], default='fiction', max_length=100)),
                ('images', models.ImageField(upload_to='books/')),
            ],
        ),
    ]

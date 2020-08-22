# Generated by Django 3.1 on 2020-08-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sketches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Used', 'Used')], max_length=50, null=True)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images_sketches')),
            ],
        ),
    ]

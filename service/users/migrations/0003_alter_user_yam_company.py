# Generated by Django 3.2.16 on 2023-03-03 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yam_reviews', '0001_initial'),
        ('users', '0002_alter_user_yam_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='yam_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='yam_reviews.yamapcompany', verbose_name='компания'),
        ),
    ]
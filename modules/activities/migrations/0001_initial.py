# Generated by Django 3.1.7 on 2021-03-01 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated.', verbose_name='updated at')),
                ('schedule', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=35)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='properties.property')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last updated.', verbose_name='updated at')),
                ('answers', models.JSONField()),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='activities.activity')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]

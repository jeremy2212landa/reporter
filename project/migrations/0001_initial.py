# Generated by Django 4.1.2 on 2022-11-08 04:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('scope', models.CharField(default=None, max_length=100)),
                ('description', models.CharField(default=None, max_length=100)),
                ('projecttype', models.CharField(default=None, max_length=100)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('companyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.company')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vulnerabilityname', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('vulnerabilityseverity', models.CharField(max_length=300, null=True)),
                ('cvssscore', models.FloatField(blank=True, null=True)),
                ('cvssvector', models.CharField(default=None, max_length=300, null=True)),
                ('status', models.CharField(max_length=300, null=True)),
                ('vulnerabilitydescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('POC', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(default=None, editable=False, null=True)),
                ('vulnerabilitysolution', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('vulnerabilityreferlnk', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerableinstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('Paramter', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('vulnerabilityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.vulnerability')),
            ],
        ),
    ]
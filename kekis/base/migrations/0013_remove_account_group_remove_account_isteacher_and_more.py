# Generated by Django 4.2.1 on 2023-11-07 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_account_rank_alter_account_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='group',
        ),
        migrations.RemoveField(
            model_name='account',
            name='isTeacher',
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='competitions',
            name='current',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AddField(
            model_name='group',
            name='pupils',
            field=models.ManyToManyField(blank=True, null=True, to='base.account'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='size',
            field=models.CharField(default='M', max_length=11),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('login', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('size', models.CharField(max_length=10)),
                ('city', models.CharField(default='none', max_length=255)),
                ('favorite', models.ManyToManyField(blank=True, null=True, to='base.competitions')),
            ],
            options={
                'unique_together': {('email', 'login', 'password', 'age', 'name')},
            },
        ),
        migrations.AddField(
            model_name='group',
            name='teachers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.teacher'),
        ),
    ]

# Generated by Django 3.1.5 on 2022-03-04 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userweb', '0003_auto_20220218_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='名称')),
                ('icon', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='图标')),
                ('order', models.IntegerField(blank=True, default=1, null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
                'db_table': 'user_Menu',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='名称')),
                ('url', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='URL')),
                ('order', models.IntegerField(blank=True, default=1, null=True, verbose_name='排序')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='userweb.menu', verbose_name='菜单')),
                ('roles', models.ManyToManyField(blank=True, default=None, null=True, to='userweb.Roles', verbose_name='角色')),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permission',
                'db_table': 'user_Permission',
                'managed': True,
            },
        ),
    ]

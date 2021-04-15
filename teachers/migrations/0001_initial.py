# Generated by Django 3.2 on 2021-04-15 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
                ('archivements', models.ManyToManyField(db_table='teacher_archivement', related_name='teachers', to='persons.Achievement')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persons.personinfo')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]

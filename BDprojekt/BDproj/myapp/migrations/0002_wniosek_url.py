# Generated by Django 5.1.3 on 2024-11-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wniosek_url',
            fields=[
                ('id_wniosek', models.AutoField(primary_key=True, serialize=False)),
                ('data_poczatkowa', models.DateField()),
                ('data_koncowa', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('data_zalozenia', models.DateField()),
                ('Uzytkownik_id_uzytkownika', models.IntegerField()),
            ],
            options={
                'db_table': 'wniosek_url',
                'managed': False,
            },
        ),
    ]

# Generated by Django 3.0.7 on 2020-11-02 09:49

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('farm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fur',
            fields=[
                ('fur_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sort', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fur_shop.Farm')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=300)),
                ('fur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fur_shop.Fur')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('coat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fur_shop.Fur')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]

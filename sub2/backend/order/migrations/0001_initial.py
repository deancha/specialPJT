# Generated by Django 2.2.7 on 2020-10-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('tid', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=10)),
                ('kakaoemail', models.CharField(max_length=100)),
                ('liquornumber', models.IntegerField()),
                ('liquorname', models.CharField(max_length=100)),
                ('liquorprice', models.IntegerField(default=1)),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('waynumber', models.CharField(default='-', max_length=80)),
                ('uniqueness', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField()),
                ('status', models.CharField(default='배송전', max_length=30)),
            ],
        ),
    ]
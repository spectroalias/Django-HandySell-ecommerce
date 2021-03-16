# Generated by Django 3.1.7 on 2021-03-10 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('add_line_1', models.CharField(max_length=120)),
                ('add_line_2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('pincode', models.CharField(max_length=120)),
                ('country', models.CharField(choices=[('india', 'India'), ('uk', 'UK')], max_length=120)),
                ('billing_profle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billprofile.billingprofile')),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2023-05-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.TextField(max_length=50)),
                ('product_category', models.CharField(choices=[('grocery', 'grocery'), ('vegetables', 'vegetables'), ('fruits', 'fruits'), ('chocolates', 'chocolates')], default='grocery', max_length=50, null=True)),
                ('product_quantity', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('product_price', models.DecimalField(decimal_places=3, max_digits=50, null=True)),
                ('product_description', models.TextField(max_length=50)),
                ('product_image', models.ImageField(upload_to='profile/')),
            ],
        ),
        migrations.RenameModel(
            old_name='customer',
            new_name='admin_registration',
        ),
        migrations.RenameField(
            model_name='admin_registration',
            old_name='customer_confirmpassword',
            new_name='adminaddress',
        ),
        migrations.RenameField(
            model_name='admin_registration',
            old_name='customer_email',
            new_name='adminconfirmpassword',
        ),
        migrations.RenameField(
            model_name='admin_registration',
            old_name='customer_name',
            new_name='admincontact',
        ),
        migrations.RenameField(
            model_name='admin_registration',
            old_name='customer_password',
            new_name='adminname',
        ),
        migrations.RenameField(
            model_name='admin_registration',
            old_name='customer_phonenumber',
            new_name='adminpassword',
        ),
        migrations.RenameField(
            model_name='admin_registration',
            old_name='customer_username',
            new_name='adminusername',
        ),
    ]

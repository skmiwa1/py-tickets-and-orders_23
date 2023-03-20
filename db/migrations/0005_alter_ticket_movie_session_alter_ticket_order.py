# Generated by Django 4.0.2 on 2023-03-20 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_order_options_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='movie_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='db.moviesession'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='db.order'),
        ),
    ]
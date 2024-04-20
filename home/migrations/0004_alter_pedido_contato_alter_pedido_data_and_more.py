# Generated by Django 4.2.4 on 2024-04-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_pedido_campo_data_pedido_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='contato',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

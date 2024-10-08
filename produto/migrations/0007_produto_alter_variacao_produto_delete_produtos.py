# Generated by Django 4.2.4 on 2024-08-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_produtos_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_promocional', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='variacao',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto'),
        ),
        migrations.DeleteModel(
            name='Produtos',
        ),
    ]

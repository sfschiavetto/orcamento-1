from typing import Iterable
from django.db import models
import os
from django.conf import settings
# a função slugfy ajuda a criar slugs automáticos 
# um slug é uma versão de uma string, que é convertida para uma forma segura de URL
# p ex quando salvarmos um produto "Cartão de visita" será gerado o slug 'cartao-de-visita'
from django.utils.text import slugify

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True) # a ideia é utilizar o slug para gerar as URLs e listar os produtos depois
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_promocional = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(
        default= 'V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    # função para gerar e salvar slugs
    # aceita argumentos (*args) e palavras-chave (**kwargs) que possam ser passados ao método 'save' do Django 
    def save(self, *args, **kwargs):
        if not self.slug:
            # não modifica um slug criado, mas add um caso o campo esteja em branco
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save( *args, **kwargs)

class Variacao(models.Model):
    # on_delete=models.CASCADE : faz com que quando se delete um produto, delete todas as variações (cadastrar variações será implementado depois)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) 
    nome = models.CharField(max_length=30, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    class Meta: 
        verbose_name = "Variacao"
        verbose_name_plural = "Variações"

    def __str__(self):
        return self.nome or self.produto.nome

from django.db import models


class Pedido(models.Model):
    data = models.DateField()
    nome_cliente = models.CharField(max_length=100)
    contato = models.CharField(max_length=11)
    cpf_cnpj = models.CharField(max_length=14)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descricao_pedido = models.TextField()
    descricao_impresso = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Pedido de {self.nome_cliente} em {self.data}"

    class Meta:
        ordering = ['-id']  # Ordenar por data_pedido em ordem decrescente    
        

    

from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    valor_unitario = forms.DecimalField(
        label='Valor Unit. R$',
         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'R$ 0,00'}),
    )
    class Meta:
        model = Pedido
        fields = '__all__'  # Use todos os campos do modelo Pedido
        # Caso queira selecionar campos específicos:
        # fields = ['data', 'nome_cliente', 'contato', 'cpf_cnpj', 'produto', 'quantidade', 'valor_unitario', 'descricao_pedido', 'descricao_impresso', 'valor_total']
        

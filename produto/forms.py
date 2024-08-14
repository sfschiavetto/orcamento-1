from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'descricao_curta', 'descricao_longa', 'slug', 'preco', 'preco_promocional', 'tipo']

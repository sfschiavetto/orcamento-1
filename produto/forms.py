from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 
                  'descricao_curta', 
                  'descricao_longa', 
                  'slug', 
                  'preco', 
                  'preco_promocional', 
                  'tipo']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_curta': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_longa': forms.Textarea(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco_promocional': forms.NumberInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }

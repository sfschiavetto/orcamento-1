from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from .models import Pedido
from .forms import PedidoForm
from datetime import date
from datetime import datetime
from decimal import Decimal, InvalidOperation




@login_required
def all(request):
    pedidos = Pedido.objects.all()
    now = datetime.now()
    ano = str(now.year).zfill(4) 
    mes = str(now.month).zfill(2) 
    dia = str(now.day).zfill(2)
    data_atual = ano + mes + dia
    for pedido in pedidos:
        pedido.nome_cliente = pedido.nome_cliente.upper() if pedido.nome_cliente else ''
        pedido.cpf_cnpj = pedido.cpf_cnpj.upper() if pedido.cpf_cnpj else ''
        
   
    context = {
        'data_atual': data_atual,
        'pedidos': pedidos
    }
        
    return render(request, 'all.html', context )



@require_POST
def custom_logout(request):
    logout(request)
    return render ('login.html')  # Redireciona para a página de login (login.html)
    
@login_required
def base(request):
    return render(request, 'base.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autenticar o usuário
            user = form.get_user()
            auth_login(request, user)
            # Redirecionar para a página 'all.html' após o login
            return redirect('all')  # 'all' é o nome da URL para 'all.html'
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



@login_required
def criar_pedido(request):
    data_atual = datetime.now().date()  # Obter a data atual (sem hora)

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Processar a data do formulário e atribuir ao campo data_pedido
            data_str = request.POST.get('data', None)  # Obter a data do formulário
            if data_str:
                try:
                    data = date.fromisoformat(data_str)
                    form.instance.data_pedido = data  # Atribuir data ao campo data_pedido
                except ValueError:
                    # Lidar com erro de formatação de data, se necessário
                    pass

            # Processar o valor_unitario do formulário e atribuir ao campo valor_unitario
            valor_str = form.cleaned_data['valor_unitario']
            if valor_str:
                try:
                    valor = parse_decimal_br(valor_str)  # Função para converter valor monetário brasileiro em Decimal
                    form.instance.valor_unitario = valor  # Atribuir valor_unitario ao campo valor_unitario
                except ValueError:
                    # Lidar com erro de conversão de valor
                    pass
            form.save()
            return redirect('all')  # Redirecionar para página de sucesso após salvar
        
    else:
        form = PedidoForm()

    # Criar o contexto com o formulário e a data atual
    context = {
        'form': form,
        'data_atual': data_atual,
    }

    return render(request, 'criar_pedido.html', context)

def parse_decimal_br(value):
    """Função para converter valor monetário brasileiro em Decimal."""
    try:
        # Converter value para string se ainda não for uma string
        if not isinstance(value, str):
            value = str(value)
        
        # Remover caracteres não numéricos (exceto ponto e vírgula) e substituir vírgula por ponto
        numeric_chars = [c for c in value if c.isdigit() or c == ',' or c == '.']
        cleaned_value = ''.join(numeric_chars)
        decimal_value = Decimal(cleaned_value.replace(',', '.'))
        return decimal_value
    except InvalidOperation:
        raise ValueError("Valor monetário inválido")
    
@login_required
def excluir_pedido(request, pedido_id):
    # Obter o pedido pelo ID
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        # Verificar se o formulário foi submetido via POST
        # Processar a exclusão do pedido
        pedido.delete()
        # Redirecionar para uma página de sucesso ou outra view após a exclusão
        return redirect('all')

    # Se não for um POST, renderizar um template de confirmação de exclusão
    return render(request, 'confirmar_exclusao.html', {'pedido': pedido})

@login_required
def imprimir_pedido(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    now = datetime.now()
    ano = str(now.year).zfill(4) 
    mes = str(now.month).zfill(2) 
    dia = str(now.day).zfill(2)
    data_atual = ano + mes + dia
    context = {
        'data_atual': data_atual,
        'pedido': pedido
    }
    return render(request, 'impressao.html', context)
    # Exemplo simples: retornar uma mensagem de sucesso
    #return HttpResponse(f'O pedido {pedido_id} foi enviado para impressão com sucesso!')
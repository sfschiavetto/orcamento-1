from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
from .models import Produto
from .forms import ProdutoForm

# pesquisar uma forma de as messages sumirem da tela após algum tempo

def cadastrar_produto(request):
    # Verificar se o usuário está logado
    if not request.user.is_authenticated:
        return redirect ('/home/login/')

    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao_curta = request.POST.get('descricao_curta')
        descricao_longa = request.POST.get('descricao_longa')
        slug = request.POST.get('slug')
        preco = request.POST.get('preco')
        preco_promocional = request.POST.get('preco_promocional')


        try:
            # Convertendo preços para float
            preco = float(preco) if preco else 0.0
            preco_promocional = float(preco_promocional) if preco_promocional else 0.0

            # Instanciando e salvando o produto
            produto = Produto(
                nome=nome,
                descricao_curta=descricao_curta,
                descricao_longa=descricao_longa,
                slug = slug,
                preco=preco,
                preco_promocional=preco_promocional,

            )
            produto.save()
            messages.add_message(request, constants.SUCCESS, 'Produto criado com sucesso!')
            #print('salvo') para teste de fluxo no terminal
        except Exception as e:
            #print('erro') para teste de fluxo no terminal
            messages.add_message(request, constants.ERROR, 'Não foi possível cadastrar.')
        
        return redirect('/home/produto/cadastrar_produto/') 

    # Para métodos GET, renderizar o formulário
    return render(request, 'cadastrar_produto.html')


def produto_cadastrado(request):
    produtos = Produto.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'produto_cadastrado.html', {'produtos' : produtos})


def listar_produtos(request):
    produtos = Produto.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def editar_produto(request, produto_id):
    # Recuperar o código a ser editado
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        # Preencher o formulário com os dados do POST
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            # Salvar as alterações
            form.save()
            #print("ok") para teste de fluxo no terminal
            # Redirecionar para a página de códigos cadastrados
            return redirect('cadastrar_produto')
    else:
        # Se for um método GET, preencher o formulário com os dados do produto
        #print("not ok") para teste de fluxo no terminal
        form = ProdutoForm(instance=produto)
    #print("not ok") para teste de fluxo no terminal

    return render(request, 'editar_produto.html', {'form': form})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        # Redirecionar para uma página de sucesso ou outra view após a exclusão
        messages.add_message(request, messages.SUCCESS, 'Produto excluído com sucesso!')
        return redirect('listar_produtos') # podemos criar uma 'home' para o uso do redirect no futuro
    # Se não for um POST, renderizar um template de confirmação de exclusão
    
    return render(request, 'deletar_produto.html', {'produto': produto})
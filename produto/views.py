from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from .models import Produtos

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
            produto = Produtos(
                nome=nome,
                descricao_curta=descricao_curta,
                descricao_longa=descricao_longa,
                slug = slug,
                preco=preco,
                preco_promocional=preco_promocional,

            )
            produto.save()
            messages.add_message(request, constants.SUCCESS, 'Produto criado com sucesso!')
            print('salvo')
        except Exception as e:
            print('erro')
            messages.add_message(request, constants.ERROR, 'Não foi possível cadastrar.')
        
        return redirect('/home/produto/cadastrar_produto/') 

    # Para métodos GET, renderizar o formulário
    return render(request, 'cadastrar_produto.html')


def produto_cadastrado(request):
    produtos = Produtos.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'produto_cadastrado.html', {'produtos' : produtos})


def listar_produtos(request):
    produtos = Produtos.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'listar_produtos.html', {'produtos': produtos})
from django.shortcuts import render, redirect, get_object_or_404
from api.models import Produto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial ou onde preferir
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    return render(request, 'login.html')

@login_required
def home(request):
    query = request.GET.get('search', '')

    if query:
        produtos = Produto.objects.filter(
            nome__icontains=query
        ) | Produto.objects.filter(
            descricao__icontains=query
        ) | Produto.objects.filter(
            tipo__icontains=query
        ) | Produto.objects.filter(
            valor__icontains=query
        )
    else:
        produtos = Produto.objects.all()

    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        tipo = request.POST.get('tipo')
        preco = request.POST.get('preco')
        imagem = request.FILES.get('image')

        if preco:
            try:
                preco = float(preco)
            except ValueError:
                return render(request, 'home.html', {
                    'produtos': produtos,
                    'error': 'O valor do preço deve ser um número decimal válido.',
                    'search_query': query,
                })

        # Criação do produto e atribuição do usuário autenticado
        produto = Produto(
            user=request.user,  # Atribui o usuário autenticado
            nome=nome,
            descricao=descricao,
            tipo=tipo,
            valor=preco,
            imagem=imagem
        )
        produto.save()

        return redirect('home')

    context = {
        "produtos": produtos,
        "search_query": query,
    }

    return render(request, 'home.html', context)

@login_required
def editarProduto(request, id):
    produto = get_object_or_404(Produto, id=id) 

    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        tipo = request.POST.get('tipo')
        preco = request.POST.get('preco')
        imagem = request.FILES.get('image')

        if preco:
            try:
                preco = float(preco)
            except ValueError:
                return render(request, 'editar_produto.html', {
                    'produto': produto,
                    'error': 'O valor do preço deve ser um número decimal válido.',
                })

    
        produto.nome = nome
        produto.descricao = descricao
        produto.tipo = tipo
        produto.valor = preco

        if imagem:
            produto.imagem = imagem

        produto.save()
        return redirect('home')  

    context = {
        'produto': produto
    }
    return render(request, 'editarProduto.html', context)

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('home') 

    return redirect('home')
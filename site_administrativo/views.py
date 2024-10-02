from django.shortcuts import render, redirect, get_object_or_404
from api.models import Produto


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

    
        produto = Produto(nome=nome, descricao=descricao, tipo=tipo, valor=preco, imagem=imagem)
        produto.save()

  
        return redirect('site_administrativo:home')

    context = {
        "produtos": produtos,
        "search_query": query,  
    }

    return render(request, 'home.html', context)


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
        return redirect('site_administrativo:home')  

    context = {
        'produto': produto
    }
    return render(request, 'editarProduto.html', context)

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('site_administrativo:home') 

    return redirect('site_administrativo:home')
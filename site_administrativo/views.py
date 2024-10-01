from django.shortcuts import render, redirect
from api.models import Produto

def home(request):
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
                })

            produto = Produto(nome=nome, descricao=descricao, tipo=tipo, valor=preco, imagem=imagem)
            produto.save()
            return redirect('site_administrativo:home')

    context = {
        "produtos": produtos,
    }
    return render(request, 'home.html', context)
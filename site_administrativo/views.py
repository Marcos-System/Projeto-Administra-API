from django.shortcuts import render
from api.models import Produto

def home(request):
    produtos = Produto.objects.all()

    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        tipo = request.POST.get('tipo')
        preco = request.POST.get('preco')
        imagem = request.FILES.get('image')

        # Verificar se o preço foi fornecido e é um valor decimal válido
        if preco:
            try:
                preco = float(preco)  # Converter para decimal
            except ValueError:
                # Tratar o erro de conversão caso o preço seja inválido
                return render(request, 'home.html', {
                    'produtos': produtos,
                    'error': 'O valor do preço deve ser um número decimal válido.',
                })

            produto = Produto(nome=nome, descricao=descricao, tipo=tipo, valor=preco, imagem=imagem)
            produto.save()

    context = {
        "produtos": produtos,
    }
    return render(request, 'home.html', context)
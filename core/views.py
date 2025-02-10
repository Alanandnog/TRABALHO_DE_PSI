from django.shortcuts import render
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    #verificação se o formulário é válido, se não tem erros  is_valid
    if str(request.method) == "POST":
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request,'Erro ao salvar o produto')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request,'produto.html', context)


def comentarios_view(request):
    comentarios = Comentario.objects.all().order_by('-data_criacao')

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentarios')  # Redireciona para atualizar a página
    else:
        form = ComentarioForm()

    return render(request, 'comentarios.html', {'form': form, 'comentarios': comentarios})

def comentarios_produto(request, produto_id):
    # Buscar o produto e seus comentários
    return render(request, 'comentarios.html', {'produto_id': produto_id})
from django.contrib import admin

from .models import Produto

#usando um decorator para registar esse cara no admin

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque','slug', 'criado', 'modificado', 'ativo')


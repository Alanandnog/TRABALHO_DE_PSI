from django.urls import path
from .views import comentarios_produto

from.views import index, contato, produto

urlpatterns = [
    path('', index, name ='index'),
    path('contato/', contato, name ='contato'),
    path('produto/', produto, name ='produto'),
    path('comentarios/<int:produto_id>/', comentarios_produto, name='comentarios'),
]


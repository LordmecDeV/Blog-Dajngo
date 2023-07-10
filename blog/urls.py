from django.urls import path
from blog.views import index, conteudo, category_mit, category_ia, category_js, category_php

urlpatterns = [
        path('', index, name='index'),
        path('MIT', category_mit, name='mit'),
        path('IA', category_ia, name='ia'),
        path('JavaScript', category_js, name='js'),
        path('PHP', category_php, name='php'),
        path('conteudo/<int:blog_id>', conteudo, name='conteudo'),
]
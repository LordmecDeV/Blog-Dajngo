from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta
from blog.models import Blog
import requests

def index(request):
    subject = 'Django'  # Assunto da notícia que você deseja buscar
    articles = get_news(subject)
    laravel = 'Laravel'
    articles_for_laravel = get_news(laravel)
    javascript = 'Javascript'
    articles_for_javascript = get_news(javascript)
    elon_musk = 'PHP'
    articles_for_elon = get_news(elon_musk)
    framework = 'Framework'
    articles_for_framework = get_news(framework)
    node = 'Node.js'
    articles_for_node = get_news(node)
    first_article_node = articles_for_node[0] if articles_for_node else None
    first_article_framework = articles_for_framework[0] if articles_for_framework else None
    first_article_elon = articles_for_elon[0] if articles_for_elon else None
    first_article_javascript = articles_for_javascript[0] if articles_for_javascript else None
    first_article = articles[0] if articles else None
    first_article_laravel = articles_for_laravel[0] if articles_for_laravel else None
    return render(request, 'blog/index.html', {"article": first_article, "laravel": first_article_laravel, "javascript": first_article_javascript, "elon_musk": first_article_elon, "framework": first_article_framework, "node": first_article_node })

def conteudo(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/conteudo.html', {"blog": blog})

def category_mit(request):
    mit = 'MIT'
    articles_for_mit = get_news(mit)
    articles_for_mit = articles_for_mit[:10]
    return render(request, 'blog/category_mit.html', {"mit": articles_for_mit})

def category_ia(request):
    ia = 'Artificial intelligence'
    articles_for_ia = get_news(ia)
    articles_for_ia = articles_for_ia[:10]
    return render(request, 'blog/category_ia.html', {"ia": articles_for_ia})

def category_js(request):
    js = 'JavaScript'
    articles_for_js = get_news(js)
    articles_for_js = articles_for_js[:10]
    return render(request, 'blog/category_js.html', {"js": articles_for_js})

def category_php(request):
    php = 'Laravel'
    articles_for_php = get_news(php)
    articles_for_php = articles_for_php[:10]
    return render(request, 'blog/category_laravel.html', {"php": articles_for_php})

def get_news(subject):
    api_key = 'eebe3537fb8442d58bd366c174091ddc'
    query = subject  # Assunto da notícia fornecido como parâmetro

    today = date.today()  # Data atual
    last_week = today - timedelta(days=7)  # Data da última semana

    # Converter as datas para o formato esperado pela API
    from_date = last_week.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        return articles
    else:
        return []
    

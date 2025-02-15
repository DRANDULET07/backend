from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article


@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all().values()
    return Response(list(articles))


@api_view(["GET"])
def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
        return Response(
            {"title": article.title, "text": article.text, "author": article.author}
        )
    except Article.DoesNotExist:
        return Response({"error": "Article not found"}, status=404)

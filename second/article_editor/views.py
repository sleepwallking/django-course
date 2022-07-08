from django.shortcuts import render


def index(request):
    return render(request, 'article_editor/index.html')


def about(request):
    return render(request, 'article_editor/about.html')

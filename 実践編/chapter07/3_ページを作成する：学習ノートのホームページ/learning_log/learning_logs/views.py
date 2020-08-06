from django.shortcuts import render

def index(request):
    """学習ノートのホームページ"""
    return render(request, 'learning_logs/index.html')

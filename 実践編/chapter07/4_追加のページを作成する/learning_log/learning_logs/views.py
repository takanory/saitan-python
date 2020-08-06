from django.shortcuts import render

from .models import Topic

def index(request):
    """学習ノートのホームページ"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """すべてのトピックを表示する"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """1つのトピックとそれについてのすべての記事を表示"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

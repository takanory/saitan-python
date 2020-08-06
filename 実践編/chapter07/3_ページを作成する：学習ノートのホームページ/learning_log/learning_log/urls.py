"""learning_logsのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
]

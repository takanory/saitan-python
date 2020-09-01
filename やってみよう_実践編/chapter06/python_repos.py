"""作者による注記
    テストを書く場合、テストが実行できるように対象のコードを構造化することが強いられます。
    これは、すべての作業を4つの関数に書き換えた改訂版の python_repos.py です。
    訳注 : 実際は python_repos_visual.py が対象のようです。
"""
import requests

from plotly.graph_objs import Bar
from plotly import offline

def get_response():
    # API呼び出しを作成してそのレスポンスを返す
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r

def get_repo_dicts(r):
    """最も人気のあるリポジトリを表わす一連の辞書を返す"""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_project_data(repo_dicts):
    """可視化に必要な各プロジェクトのデータを返す"""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels

def make_visualization(repo_links, stars, labels):
    """最も人気のあるリポジトリの可視化を実行する"""
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'GitHubで最も多くのスターがついているPythonプロジェクト',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'リポジトリ',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'スターの数',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },

    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')

if __name__ == '__main__':
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)

"""作者による注記(プログラムコードの後に記載)
    関数の呼び出しは if ブロックの中に配置されています。このためこれらの関数は、ファイルが直接実行されたときは
    呼び出されますが、インポートされたときには呼び出されません。
    これで、これらの関数のテストを書くことができます。
    訳注 : 6_3_test_python_repos.py の「作者によるこの解答例についての注記」に続きます。
    (作者による注記は https://ehmatthes.github.io/pcc_2e/solutions/
            chapter_17/#17-3-testing-python_repospy
    に記載の文章を翻訳して掲載しました)
""" 

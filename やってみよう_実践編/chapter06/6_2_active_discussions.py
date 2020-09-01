"""作者によるこの解答例についての注記
    この演習問題を解決するためのアプローチはたくさんあります。
    ここでは、投稿を処理するコードはオリジナルをそのまま流用し、
    次に可視化のために必要なリストを生成するためにループを書きました。
    この方法では、オリジナルデータは全て保持されており、その中から
    必要な対象だけを取り出してグラフ化を行っています。
    投稿をIDごとに処理するオリジナルのループを、
    可視化に必要な情報だけを取り出すように変更することもできます。
    ( https://ehmatthes.github.io/pcc_2e/solutions/
            chapter_17/#17-2-active-discussions 
    に記載の文章を翻訳して掲載しました)
"""
from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# API呼び出しを作成してそのレスポンスを格納する
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

# 各投稿についての情報を処理する
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 投稿ごとに、別々のAPI呼び出しを作成する
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # 各記事の辞書を作成する
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nタイトル: {submission_dict['title']}")
    print(f"リンクURL: {submission_dict['hn_link']}")
    print(f"コメント数: {submission_dict['comments']}")

# グラフ作成のためにリストを生成する
titles, num_comments, discn_links = [], [], []
for sd in submission_dicts:
    title = sd['title']
    hn_link = sd['hn_link']
    discn_link = f"<a href='{hn_link}'>{title[:15]}...</a>"

    titles.append(title)
    num_comments.append(sd['comments'])
    discn_links.append(discn_link)

# 可視化を実行する
data = [{
    'type': 'bar',
    'x': discn_links,
    'y': num_comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'ハッカーニュースでもっとも議論されている記事',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '記事のタイトル',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'コメント数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_discussions.html')

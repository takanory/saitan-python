from operator import itemgetter

import requests

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

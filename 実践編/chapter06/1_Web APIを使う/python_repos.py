import requests

# API呼び出しを作成してそのレスポンスを格納する
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

# APIレスポンスを変数に格納する
response_dict = r.json()
print(f"全リポジトリ数: {response_dict['total_count']}")

# リポジトリに関する情報を調べる
repo_dicts = response_dict['items']
print(f"情報が返されたリポジトリの数: {len(repo_dicts)}")

print("\n各リポジトリの情報の抜粋:")
for repo_dict in repo_dicts:
    print(f"\n名前: {repo_dict['name']}")
    print(f"所有者: {repo_dict['owner']['login']}")
    print(f"スターの数: {repo_dict['stargazers_count']}")
    print(f"リポジトリURL: {repo_dict['html_url']}")
    print(f"説明文: {repo_dict['description']}")

# macOSでのPythonインストール手順

## 最新バージョンのPythonをインストールする
macOS用のPythonインストーラーを見つけるために、https://python.org を開きます。
「Downloads」リンクの上にマウスカーソルを移動すると、最新バージョンのPythonのダウンロード用ボタンが表示されます。
ボタンをクリックすると、OSに対応したインストーラーのダウンロードが始まります。
ファイルのダウンロードが終了したら、インストーラーを起動します。

インストールが終了したら、ターミナルプロンプトに次のコマンドを入力します。

```
$ python3 --version
Python 3.8.3
```

このような出力が表示されたら、Pythonを試す準備ができています。
なお、 `python` コマンドを見かけたときは、必ず `python3` を使用するようにしてください。

## Pythonをターミナル上で動かす

ターミナルを開いてpython3と入力すると、Pythonの短いコードを実行できるようになります。
Pythonの対話モードを終了する際には、 **Ctrl＋D** キーを押すか `exit()` コマンドを入力することを忘れないでください。

## Sublime Textをインストールする

Sublime Textエディターをインストールするために、Webサイト( https://sublimetext.com/ )からインストーラーをダウンロードします。
「Download」リンクをクリックし、macOS用のインストーラーを探します。
インストーラーをダウンロードしたら、そのファイルを開き、Sublime Textのアイコンをアプリケーションフォルダーにドラッグしてインストールします。

## 正しいバージョンのPythonを使用するようにSublime Textを設定する

pythonコマンドの代わりに **python3** コマンドを使用しなければならない場合は、Sublime Textが正しいバージョンのPythonを使用してプログラムを実行できるようにするための設定が必要です。

Sublime Textのアイコンをクリックするか、PCの検索バーでSublime Textを検索して起動します。
「Toolsm▶Build System▶New Build System」を選択し、新しい設定ファイルを開きます。
既存の内容を削除し、次の内容を入力します

```
{
    "cmd": ["python3", "-u", "$file"],
}
```

このコードは、Sublime TextがPythonプログラムのファイルを実行するときに **python3** コマンドを使用するように指示するものです。
ファイルを保存するときにSublime Textが開くデフォルトのフォルダーにこのファイルをPython3.sublime-buildという名前で保存します。

## Sublime Textでプログラムを実行する

**python*8 コマンドが動作する場合は、メニューから「Tools▶Build」を選択するかCommand＋Bキーを押すと、プログラムを実行できます。

Sublime Textへの設定を行った場合は、「Tools▶Build System」の中の「Python 3」を選択します。
以降は、「Tools▶Build」を選択するかCommand＋Bキーを押すとプログラムを実行できます。

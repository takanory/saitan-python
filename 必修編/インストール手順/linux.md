# LinuxでのPythonインストール手順

## Pythonのバージョンを確認する
ターミナルアプリケーションを起動します（UbuntuではCtrl＋Alt＋Tキーを押す）。
どのバージョンのPythonがインストールされているかを確認するために、小文字のpから始まる `python3` を入力します。
Pythonがインストールされている場合は、このコマンドによってPythonインタープリタが起動します。
すると、インストールされているPythonのバージョンが次のように表示され、そのあとに `>>>` プロンプトが表示されてPythonのプログラムが入力できるようになります。

```
$ python3
Python 3.8.2 (default, Apr 27 2020, 15:53:34)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

この表示は、初期状態でPCにPython 3.8.2がインストールされていることを示しています。
表示を確認したら、 **Ctrl＋D** キーを押すか `exit()` を入力してPythonプロンプトを抜け、ターミナルのプロンプトに戻ります。

## Pythonをインストールする

Pythonは多くのLinuxシステムに最初からインストールされています。
しかしデフォルトのバージョンがPython 3.6より古い場合は、最新バージョンをインストールする必要があります。
次の手順は、aptコマンドを使用できる多くのシステムで動作します。

deadsnakesと呼ばれるパッケージを使用することで、複数バージョンのPythonを簡単にインストールできます。
次のコマンドを入力します。

```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt install python3.8
```

一連のコマンドにより、PCにPython 3.8がインストールされます。
次のコマンドを実行してターミナル上でPython 3.8を実行できることを確認します。

```
$ python3.8
>>>
```

## Sublime Textをインストールする
Linuxでは、Ubuntu Software CenterからSublime Textをインストールできます。
メニューのUbuntu Softwareアイコンをクリックし、 **Sublime Text**を検索します。クリックしてインストールしたら、Sublime Textを起動します。

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

**python*8 コマンドが動作する場合は、メニューから「Tools▶Build」を選択するかCtrl＋Bキーを押すと、プログラムを実行できます。

Sublime Textへの設定を行った場合は、「Tools▶Build System」の中の「Python 3」を選択します。
以降は、「Tools▶Build」を選択するかCtrl＋Bキーを押すとプログラムを実行できます。

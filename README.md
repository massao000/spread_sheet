# Googleスプレッドシートの操作

![img](https://user-images.githubusercontent.com/69783019/112752730-5d59af80-900f-11eb-8053-44bacb5e8deb.png)

## 概要
Google APIsを使ってアニメ管理ができるデータベース風のアプリケーションです。

## ファイル概要
main.py メインプログラムファイル

* package メインで動かす関数のまとめる場所
    * check.py
    * program.py

spreadsheet_key.txt 
* `docs.google.com/spreadsheets/d/{xxxxxxxx}/edit`
 {xxxxxxxx}の部分が書かれたテキストファイル


animation_db.xlsx アプリ用のスプレッドシート


# 事前準備
スプレッドシートを操作できるように [Google Cloud Platform](https://console.cloud.google.com/apis/library?folder=&organizationId=&project=tidal-mode-303814) の設定
（時間があれば最新版の設定方法を作る予定）

参考
* [【もう迷わない】Pythonでスプレッドシートに読み書きする初期設定まとめ](https://tanuhack.com/operate-spreadsheet/)

spreadsheet_key.txtにシートURLの
`docs.google.com/spreadsheets/d/{`**<font color="Red">xxxxxxxx</font>**`}/edit`
{**xxxxxxxx**}部分を保存しておく

# 機能
動作YouTube[]()

* スプレッドシートの書き込み
* スプレッドシートの書き換え
* スプレッドシートの個別書き換え
* スプレッドシートの行の消去


# 使用した ライブラリ
* [gspread](https://gspread.readthedocs.io/en/latest/)
 スプレッドシートを操作するライブラリ

* [oauth2client](https://oauth2client.readthedocs.io/en/latest/)
 GoogleAPIの認証関連のライブラリ
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
 HTMLやXMLから情報を抽出するライブラリ
* [requests](https://pypi.org/project/requests/)
 webサイトの情報が簡単に取得できるライブラリ
* [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
 Pythonで簡単なコードかつシンプルにできるGUIライブラリ
* [string](https://pypi.org/project/strings/)
 文字列操作ライブラリ
* [webbrowser](https://docs.python.org/ja/3/library/webbrowser.html)
 webベースのドキュメントを表示ライブラリ

# 備考

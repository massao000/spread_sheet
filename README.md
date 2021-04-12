
# Googleスプレッドシートの操作

## 概要
Google APIsを使ってアニメ管理ができるデータベース風のアプリケーションです。


# 事前準備
* スプレッドシートを操作できるように [Google Cloud Platform](https://console.cloud.google.com/apis/library?folder=&organizationId=&project=tidal-mode-303814) の設定

* 参考　[【もう迷わない】Pythonでスプレッドシートに読み書きする初期設定まとめ](https://tanuhack.com/operate-spreadsheet/)

* 上記での設定でGoogle Cloud Platformのアカウントキー(jsonファイル)とスプレッドシート(私のanimation_db.xlsx)が必要です。

* spreadsheet_key.txtにシートURLの
`docs.google.com/spreadsheets/d/{`**<font color="Red">xxxxxxxx</font>**`}/edit`
{**xxxxxxxx**}部分を保存しておく

# 動作＆機能
![GIF](https://user-images.githubusercontent.com/69783019/114362948-dc73e980-9bb2-11eb-91fa-ad4d3c670857.gif)

main.exeファイルを使えばライブラリのDLは不要です。

書き込み、書き換え、個別書き換え、行の消去がどう動くか確認用に[YouTube](https://www.youtube.com/embed/DTH6uXplb9A)に動画を載せておきました

* スプレッドシートを見なくても操作が可能になっている

* 簡単にアニメの公式サイトとwikiのURLのがスプレッドシートにかきこまれる(おまけ程度のもの)

* スプレッドシートの書き込み、書き換え、個別書き換え、行の消去

# メニュー画面
![img](https://user-images.githubusercontent.com/69783019/112752730-5d59af80-900f-11eb-8053-44bacb5e8deb.png)
![image](https://user-images.githubusercontent.com/69783019/112761836-087e5f00-9038-11eb-9b77-dd48e4dffa70.png)
![image](https://user-images.githubusercontent.com/69783019/112761838-0d431300-9038-11eb-90cc-f01bd6e4556c.png)
![image](https://user-images.githubusercontent.com/69783019/112762046-ce618d00-9038-11eb-86b1-4fba53a70f95.png)

# ファイル概要
main.exe exeファイル

main.py メインプログラムファイル

* package メインで動かす関数のまとめる場所
    * check.py
    * program.py

spreadsheet_key.txt 
* `docs.google.com/spreadsheets/d/{xxxxxxxx}/edit`
 {xxxxxxxx}の部分が書かれたテキストファイル


animation_db.xlsx アプリ用のスプレッドシート

# 使用した 外部ライブラリ
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

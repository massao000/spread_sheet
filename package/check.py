def period(values):
    period = ""
    if values[4] == True:
        period = '1期'
    elif values[5] == True:
        period = '2期'
    elif values[6] == True:
        period = '3期'
    elif values[7] == True:
        period = '4期'
    elif values[8] == True:
        period = '5期以上'
    elif values[9] == True:
        period = '短編'
    elif values[10] == True:
        period = '長期'
    elif values[11] == True:
        period = '映画'
    
    return period

def watching_nau(values):
    watching = ''
    if values[1] == True:
        watching = '未視聴'
    elif values[2] == True:
        watching = '視聴中'
    elif values[3] == True:
        watching = '視聴済み'
    return watching

def genre(values, category):
    name = ""
    if values == "アニメジャンル1":
        name = 'null'
    elif values == "アニメジャンル2":
        name = 'null'
    else:
        while True:
            for number, i in enumerate(category, 1):
                if i == values:
                    return number
                else:
                    continue
        # if values == 'SF/ファンタジー':
        #     return 1
        # elif values == 'メカ/ロボット':
        #     return 2
        # elif values == 'アクション/バトル':
        #     return 3
        # elif values == 'コメディ/ギャグ':
        #     return 4
        # elif values == '恋愛/ラブコメ':
        #     return 5
        # elif values == '日常/ほのぼの':
        #     return 6
        # elif values == 'スポーツ/競技':
        #     return 7
        # elif values == 'ホラー/サスペンス/推理':
        #     return 8
        # elif values == '歴史/戦記':
        #     return 9
        # elif values == '戦争/ミリタリー':
        #     return 10
        # elif values == 'ドラマ/青春':
        #     return 11
        # elif values == 'ショート':
        #     return 12
        # elif values == '百合(GL)':
        #     return 13
        # elif values == 'BL':
        #     return 14
        # elif values == 'ハーレム':
        #     return 15
        # elif values == '異世界':
        #     return 16
        # elif values == 'アイドル':
        #     return 17
        # elif values == '音楽':
        #     return 18
        # elif values == '学園':
        #     return 19
        # elif values == '戦艦':
        #     return 20
    return name
    
def text_change(ters):
    if values['line']:
        pass

# def setting_check(values):
#     if values == 'jsonfile':
#         sg.popup('jsonファイルが選択されていません', button_color=('midnightblue', '#87cefa'))
#         return 'null'

#     elif values == 'spkey':
#         sg.popup('スプレッドシートキーが入力されていません', button_color=('midnightblue', '#87cefa'))
#         return 'null'
    
#     elif values == 'tatal':
#         sg.popup('アニメタイトルが入力されていません', button_color=('midnightblue', '#87cefa'))
#         return 'null'
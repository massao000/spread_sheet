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
    return name

def edit(selection, category):
    while True:
        alphabet = [chr(i) for i in range(65, 65 + len(category))]
        for number, i in enumerate(zip(category, alphabet), 1):
            if i[0] == selection:
                return i[1]
            else:
                continue
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
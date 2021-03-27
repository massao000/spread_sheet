import re

def period(values, keyName):
    for i in values:
        if i[1] == True and re.search(f'{keyName}1', str(i[0])):
            return 1 # 1期
        elif i[1] == True and re.search(f'{keyName}2', str(i[0])):
            return 2 # 2期
        elif i[1] == True and re.search(f'{keyName}3', str(i[0])):
            return 3 # 3期
        elif i[1] == True and re.search(f'{keyName}4', str(i[0])):
            return 4 # 4期
        elif i[1] == True and re.search(f'{keyName}5', str(i[0])):
            return 5 # 5期以上
        elif i[1] == True and re.search(f'{keyName}6', str(i[0])):
            return 6 # 短編
        elif i[1] == True and re.search(f'{keyName}7', str(i[0])):
            return 7 # 長期
        elif i[1] == True and re.search(f'{keyName}8', str(i[0])):
            return 8 # 映画

def watching_number(values, keyName):
    for i in values:
        if i[1] == True and re.search(f'{keyName}1', str(i[0])):
            return 1 # 未視聴
        elif i[1] == True and re.search(f'{keyName}2', str(i[0])):
            return 2 # 視聴中
        elif i[1] == True and re.search(f'{keyName}3', str(i[0])):
            return 3 # 視聴済み

def seasons_number(values, keyName):
    for i in values:
        if i[1] == True and re.search(f'{keyName}0', str(i[0])):
            return 0 # なし
        elif i[1] == True and re.search(f'{keyName}1', str(i[0])):
            return 1 # 春
        elif i[1] == True and re.search(f'{keyName}2', str(i[0])):
            return 2 # 夏
        elif i[1] == True and re.search(f'{keyName}3', str(i[0])):
            return 3 # 秋
        elif i[1] == True and re.search(f'{keyName}4', str(i[0])):
            return 4 # 冬


def favorite_number(values, keyName):
    for i in values:
        if i[1] == True and re.search(f'{keyName}1', str(i[0])):
            return 0 # なし
        elif i[1] == True and re.search(f'{keyName}2', str(i[0])):
            return 1 # お気に入り
    # def watching_nau(values):
#     if values[1] == True:
#         return '未視聴'
#     elif values[2] == True:
#         return '視聴中'
#     elif values[3] == True:
#         return '視聴済み'

def genre(values, category):
    if values == "アニメジャンル1" or values == "なし":
        return 0
    elif values == "アニメジャンル2" or values == "なし":
        return 0
    else:
        while True:
            for number, i in enumerate(category, 0):
                if i == values:
                    return number
                else:
                    continue

def edit(selection, category):
    while True:
        alphabet = [chr(i) for i in range(65, 65 + len(category))]
        for number, i in enumerate(zip(category, alphabet), 1):
            if i[0] == selection:
                return i[1]
            else:
                continue

# def period_second(values):
#     if values[0] == True:
#         return '1期'
#     elif values[1] == True:
#         return '2期'
#     elif values[2] == True:
#         return '3期'
#     elif values[3] == True:
#         return '4期'
#     elif values[4] == True:
#         return '5期以上'
#     elif values[5] == True:
#         return '短編'
#     elif values[6] == True:
#         return '長期'
#     elif values[7] == True:
#         return '映画'

# def watching_nau_second(values):
#     for x, i in enumerate(x.items(), 1):
#         if i[1] == True and x == 1:
#             return '未視聴'
#         elif i[1] == True and x == 2:
#             return '視聴中'
#         elif i[1] == True and x == 3:
#             return '視聴済み'

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
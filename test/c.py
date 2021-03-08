import PySimpleGUI as sg

sg.theme('Dark Blue 3')

check_dic = {
    '1': 'aaa',
    '2': 'bbb',
    '3': 'ccc',
}

layout = [
    [sg.Text('読み込むテキストファイルを選択してください', size=(45, 1))],
    [sg.Check(item[1], key=item[0]) for item in check_dic.items()],
    [sg.Button('popup', key='-POPUP-')],
]

# ウィンドウ生成
window = sg.Window('動的にコントロールを配置する', layout)
index = 0

while True:
    event, values = window.read()

    if event is None:
        break

    if event == '-POPUP-':
        disp_text = ''

        #valuesの中身(aaaだけ選択された場合)
        #{'1': True, '2': False, '3': False}
        for value in values.items():

            # True(選択されている)の場合は文字列を表示するため、ちょっとだけ加工
            if value[1]:
                if not disp_text == '':
                    disp_text += ', '
                disp_text += check_dic[value[0]]

        # 選択されているかどうかで表示メッセージを変更
        if disp_text == '':
            sg.popup_ok('何も選ばれていません。')
        else:
            sg.popup_ok(disp_text + 'が選ばれています。')

db.close()

# ウィンドウ破棄
window.close()
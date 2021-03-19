from package import *

sg.theme("dark blue")

genre_list = ['SF/ファンタジー', 'メカ/ロボット', 'アクション/バトル', 'コメディ/ギャグ', 
              '恋愛/ラブコメ', '日常/ほのぼの', 'スポーツ/競技', 'ホラー/サスペンス/推理',
              '歴史/戦記', '戦争/ミリタリー', 'ドラマ/青春', 'ショート',
              '百合(GL)', 'BL', 'ハーレム', '異世界',
              'アイドル', '音楽', '学園', '戦艦'
             ]

x_list = {'SF/ファンタジー': 1, 'メカ/ロボット': 2, 'アクション/バトル': 3, 'コメディ/ギャグ': 4, 
              '恋愛/ラブコメ': 5, '日常/ほのぼの': 6, 'スポーツ/競技': 7, 'ホラー/サスペンス/推理': 8,
              '歴史/戦記': 9, '戦争/ミリタリー': 10, 'ドラマ/青春': 11, 'ショート': 12,
              '百合(GL)': 13, 'BL': 14, 'ハーレム': 15, '異世界': 16,
              'アイドル': 17, '音楽': 18, '学園': 19, '戦艦': 20
            }


x_layout = [
        [sg.Text('jsonファイル', size=(17, 1)), sg.Input('ボタンを押してjson選択->'), sg.FileBrowse('ファイル選択', key='jsonfile', button_color=('midnightblue', '#87cefa'), file_types=(("json Files", ".json"),))],
        [sg.Text('スプレッドシートキー', size=(17, 1)), sg.Input('', key='spkey'), sg.FileBrowse('ファイル選択', key='shfile', button_color=('midnightblue', '#87cefa'), file_types=(("txt Files", ".txt"),))],
        [sg.Text('シート', size=(17, 1)), sg.Combo(('シート１', 'シート２', 'シート３', 'シート４'), default_value='シート１', size=(10, 1), key='sheet')],
        ]

tab1_layout = [
        [sg.Text('アニメタイトル', size=(17, 1)), sg.InputText('銀魂', key='tatal')],
        [sg.Frame(layout=[
                         [sg.Radio('未視聴', "RADIO1"), sg.Radio('視聴中', "RADIO1"), sg.Radio('視聴済み', "RADIO1", default=True)],
                         ], title='視聴状態'), 
                            sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='genre_first'),
                            sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='genre_second')],
        [sg.Frame(layout=[
        [sg.Radio('1期', "RADIO2", default=True), sg.Radio('2期', "RADIO2"), sg.Radio('3期', "RADIO2"), sg.Radio('4期', "RADIO2"), sg.Radio('5期以上', "RADIO2"), sg.Radio('短編', "RADIO2"), sg.Radio('長期', "RADIO2"), sg.Radio('映画', "RADIO2")]
        ], title='何期か選択')],
        [sg.Button('実行ボタン', pad=(235, 13), size=(17,1), button_color=('midnightblue', '#87cefa'))]
    ]

tab2_layout =[
    [sg.Text('シートを表示中はこちらの画面の操作はできません。')],
    [sg.Text('スプレッドシートの表示'), sg.Button('表示', button_color=('midnightblue', '#87cefa'), key='display')],
    ]

tab3_layout =[
    [sg.Text('作成中', justification='center', font=('Helvetica', 70), size=(11,1))],
    [sg.Text('取得した表から更新したい所の選択する')],
    ]

tab4_layout =[
    [sg.Text('作成中', justification='center', font=('Helvetica', 70), size=(11,1))],
    [sg.Text('消去したい列を選択し列を消去する')]
    ]

tab5_layout = [
    [sg.Text('作成中', justification='center', font=('Helvetica', 70), size=(11,1))],
    [sg.Text('https://github.com/massao000',font=('default 12 underline'), text_color='skyblue', enable_events=True, key='link')]
    ]


layout = [
    [sg.Frame('設定', x_layout)],
    [sg.TabGroup([
        [sg.Tab('書き込み', tab1_layout), 
        sg.Tab('表示', tab2_layout), 
        sg.Tab('更新', tab3_layout), 
        sg.Tab('消去', tab4_layout),
        sg.Tab('設定', tab5_layout)]]
    )]
    ]

# [sg.Text('(Almost) All widgets in one Window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)]
window = sg.Window('アニメ管理', layout)
window['link'].set_cursor(cursor='hand2')
while True:
    event, values = window.read()

    print(event, values)
    # print(values['spkey'])
    # print(values['shfile'])
    # if event == sg.WIN_CLOSED:
    #     break
    if event is None:
        break
    
    try:
        if values['shfile'][-4:] == '.txt':
            with open(values['spkey'], 'r', encoding='UTF-8') as f:
                values['spkey'] = f.read()
                # print('ok')
                # print(values['spkey'])
    except :
        sg.popup_error('一度ファイル選択からtxtファイルを選択したら\nそれ以降ファイルから選択をお願いします', title='file error')
        continue

        ##### タブ５ #####
    if event == 'link':
        webbrowser.open(window['link'].DisplayText)

    if values['jsonfile'] == '':
        sg.popup_error('jsonファイルが選択されていません', title='file error')
        continue

    elif values['spkey'] == '':
        sg.popup_error('スプレッドシートキーが入力されていません', title='file error')
        continue
    
    elif values['tatal'] == '':
        sg.popup_error('アニメタイトルが入力されていません', title='file error')
        continue

    jsonf = values['jsonfile']
    spread_sheet_key = values['spkey']
    exists_sheet_key = f'https://docs.google.com/spreadsheets/d/{spread_sheet_key}/edit#gid=0'

    test = requests.get(exists_sheet_key).status_code
    print(test)
    # tryを使って処理をさせる
    if test != 404:
        try:
            if values['sheet'] == 'シート１':
                ws = connect_gspread(jsonf,spread_sheet_key).get_worksheet(0)
            elif values['sheet'] == 'シート２':
                ws = connect_gspread(jsonf,spread_sheet_key).get_worksheet(1)
            elif values['sheet'] == 'シート３':
                ws = connect_gspread(jsonf,spread_sheet_key).get_worksheet(2)
            elif values['sheet'] == 'シート４':
                ws = connect_gspread(jsonf,spread_sheet_key).get_worksheet(3)
        except:
            sg.popup_error('jsonファイルが正しくありません')
            continue
    else:
        sg.Popup('シートが存在しません')
        continue

    if event == '実行ボタン':
        sg.Popup('デバック\n書き込み中にloading画面を出す', event, '\njsonファイル:', values['jsonfile'],'\nスプレッドシートキー:', values['spkey'],
                        '\nシート:', values['sheet'],
                        '\nアニメタイトル', values['tatal'], '\nアニメジャンル1', genre(values['genre_first'], genre_list), '\nアニメジャンル2', genre(values['genre_second'], genre_list),
                        values)
        
        wiki     = wiki_url(values['tatal'])
        official = official_url(values['tatal']) # 検索中に何かを出してもいいかも知らない

        writing  = [[values['tatal'], period(values), genre(values['genre_first'], genre_list), genre(values['genre_second'], genre_list), '年', '四季', watching_nau(values), official, wiki]]

        cell_list = ws.get_all_values()
        row_list = ws.row_values(1)
        ll = ['タイトル', 'n期ID', 'ジャンルID 1', 'ジャンルID 2', '年月日', '四季コード', '視聴コード', '公式ページ', 'wiki']
        
        if row_list != ll[0]:
            for i, value in zip(string.ascii_letters, ll):
                ws.update_acell(i + "1", value)
            for j in writing:
                ws.append_row(j)
                time.sleep(0.8)
        else:
            for j in writing:
                ws.append_row(j)
                time.sleep(0.8)

    if event == 'display': # 2枚のウィンドウが表示される
        yes_no = sg.popup_yes_no('シートを表示中はこちらの画面の操作はできません。', button_color=('midnightblue', '#87cefa'))
        # sg.PopupOKCancel('シートを表示中はこちらの画面の操作はできません。', button_color=('midnightblue', '#87cefa'))
        # print(yes_no)
        if yes_no == 'No':
            continue
        
        seat_display = ws.get_all_values()
        print(seat_display)
        # 列の取得をして
        # alphabet = [chr(i) for i in range(65, 65 + len(seat_display))]
        # alphabet = [chr(i) for i in range(65, 65 + 25)]

        count_n = [x for x, i in enumerate(seat_display)]
        # count_n = [x + 1 for x, i in enumerate(alphabet, -1)]

        alphabet_n = [chr(i) for i in range(65, 65 + len(seat_display[0]))]

        second_layout1 = [[sg.Table(seat_display[1:], headings=seat_display[0], auto_size_columns=False, vertical_scroll_only=False,
                    display_row_numbers=True,
                    header_text_color='#001e43', header_background_color='#a2c2e6',
                    def_col_width=15, num_rows=15, text_color='black',
                    background_color='#ebf6f7', alternating_row_color='#a0d8ef',
                    font=('UD デジタル 教科書体 NK-B', 13))],
                    [sg.Button('exit', button_color=('midnightblue', '#87cefa'))]
                    ]

        second_layout_update = [
            [sg.Combo((seat_display[0]), size=(23, 5), change_submits=True, key='line'), sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column')],
            [sg.Text('?', key='line_text', size=(10, 1)), sg.Text('列の'), sg.Text('?', size=(4, 1), key='column_text'), sg.Text('行の編集')],
            [sg.Input('')],
            [sg.Button('実行', button_color=('midnightblue', '#87cefa'))]
        ]

        second_layout_delete = [
            [sg.Text('test')],
        ]

        second_layout_all_update = [
            [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='all_column')],
            [sg.Text('?', size=(4, 1), key='all_column_text'), sg.Text('行の編集')],
            [sg.Text('アニメタイトル', size=(17, 1)), sg.InputText('', key='all_update_tatal')],
            [sg.Frame(layout=[
                             [sg.Radio('未視聴', "RADIO1"), sg.Radio('視聴中', "RADIO1"), sg.Radio('視聴済み', "RADIO1", default=True)],
                             ], title='視聴状態'), 
                                sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='all_update_genre_first'),
                                sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='all_update_genre_second')],
            [sg.Frame(layout=[
            [sg.Radio('1期', "RADIO2", default=True), sg.Radio('2期', "RADIO2"), sg.Radio('3期', "RADIO2"), sg.Radio('4期', "RADIO2"), sg.Radio('5期以上', "RADIO2"), sg.Radio('短編', "RADIO2"), sg.Radio('長期', "RADIO2"), sg.Radio('映画', "RADIO2")]
            ], title='何期か選択')],
            [sg.Button('実行ボタン', pad=(235, 13), size=(17,1), button_color=('midnightblue', '#87cefa'))]
        ]
                
        second_layout = [
            [sg.TabGroup([
                [sg.Tab('更新', second_layout_update),
                sg.Tab('消去', second_layout_delete),
                sg.Tab('列更新', second_layout_all_update)
                ]]
            )],
            [sg.Frame('シート', second_layout1)],
            ]

        second_Window = sg.Window('アニメ管理 読み込み', second_layout)
        while True:
            second_event, second_values = second_Window.read()

            text_elem = second_Window.FindElement('line_text')
            text_elem.Update(second_values['line'])

            text_elem = second_Window.FindElement('column_text')
            text_elem.Update(second_values['column'])
            
            text_elem = second_Window.FindElement('all_column_text')
            text_elem.Update(second_values['all_column'])
            
            print(second_event, second_values)

            if second_event is None or second_event == 'exit':
                print('eee')
                break

            if second_event == '実行':
                if second_values['line'] == '':
                    sg.popup_error('列が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                if second_values['column'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                
                x = edit(second_values['line'], seat_display[0])
                # print(type(second_values['column']))
                print(f"特定:{x}{second_values['column'] + 2}")
                for j in alphabet_n:
                    print(f"all {j}{second_values['column'] + 2}")
                


        second_Window.close()

    # col_list = ws.col_values(1)
    # print(col_list)

window.close()

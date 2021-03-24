from package import *

sg.theme("dark blue")

genre_list = ['なし', 'SF/ファンタジー', 'メカ/ロボット', 'アクション/バトル', 'コメディ/ギャグ', 
              '恋愛/ラブコメ', '日常/ほのぼの', 'スポーツ/競技', 'ホラー/サスペンス/推理',
              '歴史/戦記', '戦争/ミリタリー', 'ドラマ/青春', 'ショート',
              '百合(GL)', 'BL', 'ハーレム', '異世界',
              'アイドル', '音楽', '学園', '戦艦'
             ]

# x_list = {'SF/ファンタジー': 1, 'メカ/ロボット': 2, 'アクション/バトル': 3, 'コメディ/ギャグ': 4, 
#               '恋愛/ラブコメ': 5, '日常/ほのぼの': 6, 'スポーツ/競技': 7, 'ホラー/サスペンス/推理': 8,
#               '歴史/戦記': 9, '戦争/ミリタリー': 10, 'ドラマ/青春': 11, 'ショート': 12,
#               '百合(GL)': 13, 'BL': 14, 'ハーレム': 15, '異世界': 16,
#               'アイドル': 17, '音楽': 18, '学園': 19, '戦艦': 20
#             }

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
    [sg.Text('表の更新、消去の操作ができます')],
    [sg.Text('シートを表示中はこちらの画面の操作はできません。')],
    [sg.Text('スプレッドシートの更新＆表示'), sg.Button('表示', button_color=('midnightblue', '#87cefa'), key='display')],
    ]

# tab3_layout =[
#     [sg.Text('作成中', justification='center', font=('Helvetica', 70), size=(11,1))],
#     [sg.Text('取得した表から更新したい所の選択する')],
#     ]

# tab4_layout =[
#     [sg.Text('作成中', justification='center', font=('Helvetica', 70), size=(11,1))],
#     [sg.Text('消去したい列を選択し列を消去する')]
#     ]

tab5_layout = [
    [sg.Text('作成中', justification='center', font=('Helvetica', 70), size=(11,1))],
    [sg.Text('https://github.com/massao000',font=('default 12 underline'), text_color='skyblue', enable_events=True, key='link')]
    ]


layout = [
    [sg.Frame('設定', x_layout)],
    [sg.TabGroup([
        [sg.Tab('書き込み', tab1_layout), 
        sg.Tab('表示', tab2_layout), 
        # sg.Tab('更新', tab3_layout), 
        # sg.Tab('消去', tab4_layout),
        sg.Tab('設定', tab5_layout)]]
    )]
    ]

hiduke = str(datetime.date.today())
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
        continue

    # if values['jsonfile'] == '':
    #     sg.popup_error('jsonファイルが選択されていません', title='file error')
    #     continue

    # elif values['spkey'] == '':
    #     sg.popup_error('スプレッドシートキーが入力されていません', title='file error')
    #     continue
    
    # elif values['tatal'] == '':
    #     sg.popup_error('アニメタイトルが入力されていません', title='file error')
    #     continue

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
        if values['jsonfile'] == '':
            sg.popup_error('jsonファイルが選択されていません', title='file error')
            continue

        elif values['spkey'] == '':
            sg.popup_error('スプレッドシートキーが入力されていません', title='file error')
            continue
        
        elif values['tatal'] == '':
            sg.popup_error('アニメタイトルが入力されていません', title='file error')
            continue

        sg.Popup('デバック\n書き込み中にloading画面を出す', event, '\njsonファイル:', values['jsonfile'],'\nスプレッドシートキー:', values['spkey'],
                        '\nシート:', values['sheet'],
                        '\nアニメタイトル', values['tatal'], '\nアニメジャンル1', genre(values['genre_first'], genre_list), '\nアニメジャンル2', genre(values['genre_second'], genre_list),
                        values)
        
        wiki     = wiki_url(values['tatal'])
        official = official_url(values['tatal']) # 検索中に何かを出してもいいかも知らない

        writing  = [[hiduke, values['tatal'], period(list(values.items())[11:-1]), genre(values['genre_first'], genre_list), genre(values['genre_second'], genre_list), '四季', watching_nau(list(values.items())[6:9]), official, wiki]]

        cell_list = ws.get_all_values()
        row_list = ws.row_values(1)
        ll = ['書き込み日', 'タイトル', 'n期ID', 'ジャンルID 1', 'ジャンルID 2', '四季コード', '視聴コード', '公式ページ', 'wiki']
        
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
        sg.popup_quick_message('書き込みが完了しました')

    if event == 'display': # 2枚のウィンドウが表示される
        yes_no = sg.popup_yes_no('シートを表示中はこちらの画面の操作はできません。', button_color=('midnightblue', '#87cefa'))
        # sg.PopupOKCancel('シートを表示中はこちらの画面の操作はできません。', button_color=('midnightblue', '#87cefa'))
        # print(yes_no)
        if yes_no == 'No':
            continue
        
        seat_display = ws.get_all_values()
        print(seat_display)

        nki = ['1期', '2期', '3期', '4期', '5期以上', '短編', '長期', '映画']
        sityou = ['未視聴', '視聴中', '視聴済み']
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
            # [sg.Frame(layout=[
            #     [sg.Combo((seat_display[0]), size=(23, 5), change_submits=True, key='line'), sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column')],
            #     [sg.Text('?', key='line_text', size=(10, 1)), sg.Text('列の'), sg.Text('?', size=(4, 1), key='column_text'), sg.Text('行の編集')]], title='行列の選択')],
            [sg.Frame(layout=[
                [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column'), sg.Text(size=(4, 1), key='column_text'), sg.Text('行の編集')],
                [sg.Text('アニメタイトル'), sg.InputText(key='title_text')],
                [sg.Button('実行', key='title_ud', button_color=('midnightblue', '#87cefa'))]], title='タイトルの更新'), sg.Frame(layout=[
                    [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column2'), sg.Text(size=(4, 1), key='column_text2'), sg.Text('行の編集')],
                    [sg.Radio(i, "RADIO3") for i in nki[:4]],
                    [sg.Radio(i, "RADIO3") for i in nki[4:]],
                    # [sg.Radio('1期', "RADIO3"), sg.Radio('2期', "RADIO3"), sg.Radio('3期', "RADIO3"), sg.Radio('4期', "RADIO3")],
                    # [sg.Radio('5期以上', "RADIO3"), sg.Radio('短編', "RADIO3"), sg.Radio('長期', "RADIO3"), sg.Radio('映画', "RADIO3")],
                    [sg.Button('実行', key='period_ud', button_color=('midnightblue', '#87cefa'))]], title='何期か選択')],
            [sg.Frame(layout=[
                [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column3'), sg.Text(size=(4, 1), key='column_text3'), sg.Text('行の編集')],
                [sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='genre_first_ud')],
                [sg.Button('実行', key='genre_ud1', button_color=('midnightblue', '#87cefa'))]], title='ジャンルの更新1'), sg.Frame(layout=[
                    [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column4'), sg.Text(size=(4, 1), key='column_text4'), sg.Text('行の編集')],
                    [sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='genre_second_ud')],
                [sg.Button('実行', key='genre_ud2', button_color=('midnightblue', '#87cefa'))]], title='ジャンルの更新2'), sg.Frame(layout=[
                    [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column5'), sg.Text(size=(4, 1), key='column_text5'), sg.Text('行の編集')],
                    [sg.Radio(i, "RADIO4") for i in sityou],
                    # [sg.Radio('未視聴', "RADIO4"), sg.Radio('視聴中', "RADIO4"), sg.Radio('視聴済み', "RADIO4")],
                    [sg.Button('実行', key='status_ud', button_color=('midnightblue', '#87cefa'))]], title='視聴状態の更新')],
            [sg.Frame(layout=[
                [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column6'), sg.Text(size=(4, 1), key='column_text6'), sg.Text('行の編集')],
                [sg.InputText(key='official_url_text')],
                [sg.Button('実行', key='official_url_ud', button_color=('midnightblue', '#87cefa'))]], title='公式ページ変更'),sg.Frame(layout=[
                    [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='column7'), sg.Text(size=(4, 1), key='column_text7'), sg.Text('行の編集')],
                    [sg.InputText(key='wiki_url_text')],
                    [sg.Button('実行', key='wiki_url_ud', button_color=('midnightblue', '#87cefa'))]], title='wikiの変更')],
        ]

        second_layout_delete = [
            [sg.Text('test')],
        ]

        second_layout_all_update = [
            [sg.Frame(layout=[
                [sg.Combo(count_n[:-1], size=(5, 5), change_submits=True, key='all_column'), sg.Text(size=(4, 1), key='all_column_text'), sg.Text('行の編集')]], title='選択')],
            [sg.Text('アニメタイトル', size=(17, 1)), sg.InputText(key='all_ud_tatal')],
            [sg.Frame(layout=[
                             [sg.Radio('未視聴', "RADIO5"), sg.Radio('視聴中', "RADIO5"), sg.Radio('視聴済み', "RADIO5", default=True)],
                             ], title='視聴状態'), 
                                sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='all_ud_genre_first'),
                                sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='all_ud_genre_second')],
            [sg.Frame(layout=[
            [sg.Radio('1期', "RADIO6", default=True), sg.Radio('2期', "RADIO6"), sg.Radio('3期', "RADIO6"), sg.Radio('4期', "RADIO6"), sg.Radio('5期以上', "RADIO6"), sg.Radio('短編', "RADIO6"), sg.Radio('長期', "RADIO6"), sg.Radio('映画', "RADIO6")]
            ], title='何期か選択')],
            [sg.Button('実行ボタン', pad=(235, 13), size=(17,1), button_color=('midnightblue', '#87cefa'))]
        ]
                
        second_layout = [
            [sg.TabGroup([
                [sg.Tab('列更新', second_layout_all_update),
                sg.Tab('更新', second_layout_update),
                sg.Tab('消去', second_layout_delete),
                ]]
            )],
            [sg.Frame('シート', second_layout1)],
            ]

        second_Window = sg.Window('アニメ管理 読み込み', second_layout)
        while True:
            second_event, second_values = second_Window.read()

            # テキストの変換
            # second_Window.FindElement('line_text').Update(second_values['line'])

            second_Window.FindElement('column_text').Update(second_values['column'])
            second_Window.FindElement('column_text2').Update(second_values['column2'])
            second_Window.FindElement('column_text3').Update(second_values['column3'])
            second_Window.FindElement('column_text4').Update(second_values['column4'])
            second_Window.FindElement('column_text5').Update(second_values['column5'])
            second_Window.FindElement('column_text6').Update(second_values['column6'])
            second_Window.FindElement('column_text7').Update(second_values['column7'])
            
            second_Window.FindElement('all_column_text').Update(second_values['all_column'])
            
            # print(second_event, second_values)
            print(second_values)

            # 終了ボタン
            if second_event is None or second_event == 'exit':
                print('eee')
                break

            # タイトルの更新
            if second_event == 'title_ud':
                if second_values['column'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                # print(f"{alphabet_n[1]}{second_values['column'] + 2}")
                ws.update_acell(f"{alphabet_n[1]}{second_values['column'] + 2}", second_values['title_text'])
                sg.popup_quick_message('更新が完了しました')
            # n期の更新
            if second_event == 'period_ud':
                if second_values['column2'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                ws.update_acell(f"{alphabet_n[2]}{second_values['column2'] + 2}", period(list(second_values.items())[18:26]))
                sg.popup_quick_message('更新が完了しました')
            
            # ジャンル1の更新
            if second_event == 'genre_ud1':
                if second_values['column3'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                ws.update_acell(f"{alphabet_n[3]}{second_values['column3'] + 2}", genre(second_values['genre_first_ud'], genre_list))
                sg.popup_quick_message('更新が完了しました')
            
            # ジャンル2の更新
            if second_event == 'genre_ud2':
                if second_values['column4'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                ws.update_acell(f"{alphabet_n[4]}{second_values['column4'] + 2}", genre(second_values['genre_second_ud'], genre_list))
                sg.popup_quick_message('更新が完了しました')

            # 視聴の更新
            if second_event == 'status_ud':
                if second_values['column5'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                ws.update_acell(f"{alphabet_n[6]}{second_values['column5'] + 2}", watching_nau(list(second_values.items())[31:34]))
                sg.popup_quick_message('更新が完了しました')

            # 公式urlの更新
            if second_event == 'official_url_ud':
                if second_values['column6'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                ws.update_acell(f"{alphabet_n[7]}{second_values['column6'] + 2}", second_values['official_url_text'])
                sg.popup_quick_message('更新が完了しました')

            # wikiURLの更新
            if second_event == 'wiki_url_ud':
                if second_values['column7'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                ws.update_acell(f"{alphabet_n[8]}{second_values['column7'] + 2}", second_values['wiki_url_text'])
                sg.popup_quick_message('更新が完了しました')

            # 実行ボタンが押されたときの処理
            # if second_event == '実行':
            #     if second_values['line'] == '':
            #         sg.popup_error('列が選択されていません', button_color=('midnightblue', '#87cefa'))
            #         continue
            #     if second_values['column'] == '':
            #         sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
            #         continue
                
            #     x = edit(second_values['line'], seat_display[0])
            #     # print(type(second_values['column']))
            #     print(f"特定:{x}{second_values['column'] + 2}")
            #     sg.popup_quick_message(f'{x}{second_values["column"] + 2}更新が完了しました')
            
            # 全体更新の処理
            if second_event == '実行ボタン':
                # 更新する行が選択されていないとpopを表示させる
                if second_values['all_column'] == '':
                    sg.popup_error('行が選択されていません', button_color=('midnightblue', '#87cefa'))
                    continue
                
                # 更新する処理たち
                wiki     = wiki_url(second_values['all_ud_tatal'])
                official2 = official_url(second_values['all_ud_tatal'])
                writing2  = [hiduke, second_values['all_ud_tatal'], period(list(second_values.items())[7:15]), genre(second_values['all_ud_genre_first'], genre_list), genre(second_values['all_ud_genre_second'], genre_list), '四季', watching_nau(list(second_values.items())[2:5]), official2, wiki]
                # print(writing2)
                # print(f'{alphabet_n[0]}{second_values["all_column"] + 2}:{alphabet_n[-1]}{second_values["all_column"] + 2}')
                ds = ws.range(f'{alphabet_n[0]}{second_values["all_column"] + 2}:{alphabet_n[-1]}{second_values["all_column"] + 2}')
                for rewrite_location, update_table in zip(ds, writing2):
                    # print(rewrite_location , update_table)
                    rewrite_location.value = update_table
                ws.update_cells(ds)
                sg.popup_quick_message('更新が完了しました')
                


        second_Window.close()

    # col_list = ws.col_values(1)
    # print(col_list)

window.close()

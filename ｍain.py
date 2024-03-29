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
        [sg.Text('jsonファイル', size=(17, 1)), sg.Input(''), sg.FileBrowse('ファイル選択', key='jsonfile', button_color=('midnightblue', '#87cefa'), file_types=(("json Files", ".json"),))],
        [sg.Text('スプレッドシートキー', size=(17, 1)), sg.Input('', key='spkey'), sg.FileBrowse('ファイル選択', key='shfile', button_color=('midnightblue', '#87cefa'), file_types=(("txt Files", ".txt"),))],
        # [sg.Text('シート', size=(17, 1)), sg.Combo(('シート１', 'シート２', 'シート３', 'シート４'), default_value='シート１', size=(10, 1), key='sheet')],
        ]

tab1_layout = [
        [sg.Frame(layout=[
            [sg.Text('アニメタイトル', size=(15, 1)), sg.InputText('', key='tatal', pad=(1, 0))]
        ], title='タイトル')],
        [sg.Frame(layout=[
            [sg.Radio('なし', "SeasonsRadio", key='seasons0', default=True), sg.Radio('春', "SeasonsRadio", key='seasons1'), sg.Radio('夏', "SeasonsRadio", key='seasons2'), sg.Radio('秋', "SeasonsRadio", key='seasons3'), sg.Radio('冬', "SeasonsRadio", key='seasons4')]
        ], title='四季'), sg.Frame(layout=[
                                [sg.Radio('その他', "RADIO7", key='star1', default=True),
                                sg.Radio('お気に入り', "RADIO7", text_color='yellow', key='star2')]
                            ], title='お気に入り')],
        [sg.Frame(layout=[
                         [sg.Radio('未視聴', "RADIO1", key='viewing_rb1'), sg.Radio('視聴中', "RADIO1", key='viewing_rb2'), sg.Radio('視聴済み', "RADIO1", key='viewing_rb3', default=True)],
                         ], title='視聴状態'), sg.Frame(layout=[
                            [sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='genre_first')],
                            [sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='genre_second', pad=(5, 5))]
                            ], title='ジャンル')],
                            
        [sg.Frame(layout=[
        [sg.Radio('1期', "RADIO2", key='what_period1', default=True), sg.Radio('2期', "RADIO2", key='what_period2'), sg.Radio('3期', "RADIO2", key='what_period3'), sg.Radio('4期', "RADIO2", key='what_period4'), sg.Radio('5期以上', "RADIO2", key='what_period5'), sg.Radio('短編', "RADIO2", key='what_period6'), sg.Radio('長期', "RADIO2", key='what_period7'), sg.Radio('映画(劇場版)', "RADIO2", key='what_period8')]
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
    [sg.Text('https://github.com/massao000', font=('default 12 underline'), text_color='skyblue', enable_events=True, key='-LINK-')]
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
window = sg.Window('アニメ管理', layout, finalize=True)
window['-LINK-'].set_cursor(cursor='hand2')
while True:
    event, values = window.read()

    # print(event, values)
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
    if event == '-LINK-':
        webbrowser.open(window['-LINK-'].DisplayText)
        continue

    jsonf = values['jsonfile']
    spread_sheet_key = values['spkey']
    exists_sheet_key = f'https://docs.google.com/spreadsheets/d/{spread_sheet_key}/edit#gid=0'

    get_sheet_url = requests.get(exists_sheet_key).status_code
    # print(get_sheet_url)
    # tryを使って処理をさせる
    if get_sheet_url != 404:
        try:
#             if values['sheet'] == 'シート１':
            ws = connect_gspread(jsonf,spread_sheet_key)
            ws0 = ws.get_worksheet(0)
            # elif values['sheet'] == 'シート２':
            #     ws0 = connect_gspread(jsonf,spread_sheet_key).get_worksheet(1)
            # elif values['sheet'] == 'シート３':
            #     ws0 = connect_gspread(jsonf,spread_sheet_key).get_worksheet(2)
            # elif values['sheet'] == 'シート４':
            #     ws0 = connect_gspread(jsonf,spread_sheet_key).get_worksheet(3)
        except:
            sg.popup_error('jsonファイルが正しくありません')
            continue
    else:
        sg.Popup('シートが存在しません')
        continue
    
    ## スプレッドシートから直接とってくる
    # ws2 = ws.get_worksheet(2)
    # anime_id = ws2.col_values(2,2)
    # anime_id[0] = 'なし'
    # anime = [x for x in anime_id]
    # window.FindElement('genre_first').Update(values=anime[:], size=(23, 5))

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

        # sg.Popup('デバック\n書き込み中にloading画面を出す', event, '\njsonファイル:', values['jsonfile'],'\nスプレッドシートキー:', values['spkey'],
        #                 '\nシート:', # values['sheet'],
        #                 '\nアニメタイトル', values['tatal'], '\nアニメジャンル1', genre(values['genre_first'], genre_list), '\nアニメジャンル2', genre(values['genre_second'], genre_list),
        #                 values)
        
        wiki     = wiki_url(values['tatal'])
        official = official_url(values['tatal']) # 検索中に何かを出してもいいかも知らない

        writing  = [[hiduke, values['tatal'], period(list(values.items()), 'what_period'), genre(values['genre_first'], genre_list), genre(values['genre_second'], genre_list), seasons_number(list(values.items()), "seasons"), watching_number(list(values.items()), 'viewing_rb'), favorite_number(list(values.items()), 'star'), official, wiki]]

        cell_list = ws0.get_all_values()
        row_list = ws0.row_values(1)
        ll = ['書き込み日', 'タイトル', 'n期ID', 'ジャンルID 1', 'ジャンルID 2', '四季ID', '視聴ID', 'お気に入り', '公式ページ', 'wiki']

        if row_list != ll[0]:
            for i, value in zip(string.ascii_letters, ll):
                ws0.update_acell(i + "1", value)
            for j in writing:
                ws0.append_row(j)
                time.sleep(0.8)
        else:
            for j in writing:
                ws0.append_row(j)
                time.sleep(0.8)
        sg.popup_quick_message('書き込みが完了しました')

    if event == 'display': # 2枚のウィンドウが表示される
        yes_no = sg.popup_yes_no('シートを表示中はこちらの画面の操作はできません。', button_color=('midnightblue', '#87cefa'))
        # sg.PopupOKCancel('シートを表示中はこちらの画面の操作はできません。', button_color=('midnightblue', '#87cefa'))
        # print(yes_no)
        if yes_no == 'No':
            continue
        # ws2 = connect_gspread(jsonf,spread_sheet_key).get_worksheet(1)
        
        seat_display = ws0.get_all_values()
        # print(seat_display)
        ws1 = ws.get_worksheet(1)
        id_list = ws1.get_all_values()

        # nki          = ['1期', '2期', '3期', '4期', '5期以上', '短編', '長期', '映画(劇場版)']
        # sityou       = ['未視聴', '視聴中', '視聴済み']
        # four_seasons = ['春', '夏', '秋', '冬']
        # 列の取得をして
        # alphabet = [chr(i) for i in range(65, 65 + len(seat_display))]
        # alphabet = [chr(i) for i in range(65, 65 + 25)]
        try:
            count_n = [x for x, i in enumerate(seat_display)]
            # count_n = [x + 1 for x, i in enumerate(alphabet, -1)]

            alphabet_n = [(chr(alphabet), numbers) for numbers, alphabet in enumerate(range(65, 65 + len(seat_display[0])))]

            alphabet_n2 = [chr(i) for x, i in enumerate(range(65, 65 + len(id_list[0])))]
        except:
            sg.popup_error('書き込みを先に行ってください')
            continue
        
        # alphabet_number = [i for i in range(65, 65 + len(seat_display[0]))]

        second_layout1 = [[sg.Table(seat_display[1:], headings=seat_display[0], auto_size_columns=False, vertical_scroll_only=False,
                    display_row_numbers=True,
                    header_text_color='#001e43', header_background_color='#a2c2e6',
                    def_col_width=14, num_rows=15, text_color='black',
                    background_color='#ebf6f7', alternating_row_color='#a0d8ef',
                    font=('UD デジタル 教科書体 NK-B', 13), key='-TableUpdate-')],
                    [sg.Button('exit', size=(20, 1), font=('HGS創英角ゴシックUB', 30), button_color=('midnightblue', '#87cefa'))]
                    ]

        second_layout_update = [
            # [sg.Frame(layout=[
            #     [sg.Combo((seat_display[0]), size=(23, 5), change_submits=True, key='line'), sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column')],
            #     [sg.Text('?', key='line_text', size=(10, 1)), sg.Text('列の'), sg.Text('?', size=(4, 1), key='column_text'), sg.Text('行の編集')]], title='行列の選択')],
            [sg.Frame(layout=[
                [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column'), sg.Text(size=(4, 1), key='column_text'), sg.Text('行の編集')],
                [sg.Text('アニメタイトル'), sg.InputText(key='title_text')],
                [sg.Button('実行', key='title_ud', button_color=('midnightblue', '#87cefa'))]], title='タイトルの更新'), sg.Frame(layout=[
                    [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column2'), sg.Text(size=(4, 1), key='column_text2'), sg.Text('行の編集')],
                    # [sg.Radio(i, "RADIO3", key='ud_what_period1') for i in nki[:4]],
                    # [sg.Radio(i, "RADIO3", key='ud_what_period5') for i in nki[4:]],
                    [sg.Radio('1期', "RADIO3", key='ud_what_period1', default=True), sg.Radio('2期', "RADIO3", key='ud_what_period2'), sg.Radio('3期', "RADIO3", key='ud_what_period3'), sg.Radio('4期', "RADIO3", key='ud_what_period4')],
                    [sg.Radio('5期以上', "RADIO3", key='ud_what_period5'), sg.Radio('短編', "RADIO3", key='ud_what_period6'), sg.Radio('長期', "RADIO3", key='ud_what_period7'), sg.Radio('映画(劇場版)', "RADIO3", key='ud_what_period8')],
                    [sg.Button('実行', key='period_ud', button_color=('midnightblue', '#87cefa'))]], title='何期か選択')],
            [sg.Frame(layout=[
                [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column3'), sg.Text(size=(4, 1), key='column_text3'), sg.Text('行の編集')],
                [sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='genre_first_ud')],
                [sg.Button('実行', key='genre_ud1', button_color=('midnightblue', '#87cefa'))]], title='ジャンルの更新1'), sg.Frame(layout=[
                    [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column4'), sg.Text(size=(4, 1), key='column_text4'), sg.Text('行の編集')],
                    [sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='genre_second_ud')],
                [sg.Button('実行', key='genre_ud2', button_color=('midnightblue', '#87cefa'))]], title='ジャンルの更新2'), sg.Frame(layout=[
                    [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column5'), sg.Text(size=(4, 1), key='column_text5'), sg.Text('行の編集')],
                    [sg.Radio('未視聴', "RADIO4", key='ud_viewing_rb1'), sg.Radio('視聴中', "RADIO4", key='ud_viewing_rb2'), sg.Radio('視聴済み', "RADIO4", key='ud_viewing_rb3', default=True)],
                    # [sg.Radio(i, "RADIO4") for i in sityou],
                    [sg.Button('実行', key='status_ud', button_color=('midnightblue', '#87cefa'))]], title='視聴状態の更新')],
            [sg.Frame(layout=[
                [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='seasons_column'), sg.Text(size=(4, 1), key='seasons_text_n'), sg.Text('行の編集')],
                [sg.Radio('その他', "SeasonsRadio3", key='ud_seasons0', default=True), sg.Radio('春', "SeasonsRadio3", key='ud_seasons1'), sg.Radio('夏', "SeasonsRadio3", key='ud_seasons2'), sg.Radio('秋', "SeasonsRadio3", key='ud_seasons3'), sg.Radio('冬', "SeasonsRadio3", key='ud_seasons4')],
                [sg.Button('実行', key='seasons_key', button_color=('midnightblue', '#87cefa'))]], title='四季の更新'), sg.Frame(layout=[
                            [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='ud_stars_column'), sg.Text(size=(4, 1), key='ud_stars_text'), sg.Text('行の編集')],
                            [sg.Radio('なし', "StarRADIO2", key='ud_star1', default=True),
                            sg.Radio('お気に入り', "StarRADIO2", text_color='yellow', key='ud_star2')],
                            [sg.Button('実行', key='ud_star_b', button_color=('midnightblue', '#87cefa'))]
                        ], title='お気に入り')],
            [sg.Frame(layout=[
                [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column6'), sg.Text(size=(4, 1), key='column_text6'), sg.Text('行の編集')],
                [sg.InputText(key='official_url_text')],
                [sg.Button('実行', key='official_url_ud', button_color=('midnightblue', '#87cefa'))]], title='公式ページ更新'),sg.Frame(layout=[
                    [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='column7'), sg.Text(size=(4, 1), key='column_text7'), sg.Text('行の編集')],
                    [sg.InputText(key='wiki_url_text')],
                    [sg.Button('実行', key='wiki_url_ud', button_color=('midnightblue', '#87cefa'))]], title='wikiの更新')],
        ]


        second_layout_all_update = [
            [sg.Frame(layout=[
                [sg.Combo(values=(count_n[:-1]), size=(5, 5), change_submits=True, key='all_column'), sg.Text(size=(4, 1), key='all_column_text'), sg.Text('行の編集')]], pad=(13, 13), title='選択')],
            [sg.Frame(layout=[[sg.Text('アニメタイトル', size=(17, 1)), sg.InputText(key='all_ud_tatal')]], pad=(13, 13), title='タイトル更新')],
            [sg.Frame(layout=[
                [sg.Radio('その他', "SeasonsRadio2", key='all_seasons0', default=True), sg.Radio('春', "SeasonsRadio2", key='all_seasons1'), sg.Radio('夏', "SeasonsRadio2", key='all_seasons2'), sg.Radio('秋', "SeasonsRadio2", key='all_seasons3'), sg.Radio('冬', "SeasonsRadio2", key='all_seasons4')]], title='四季', pad=(13, 13)), sg.Frame(layout=[
                    [sg.Radio('なし', "StarRADIO3", key='all_ud_star1', default=True), sg.Radio('お気に入り', "StarRADIO3", text_color='yellow', key='all_ud_star2')]
                    ], title='お気に入り')],
            [sg.Frame(layout=[
                             [sg.Radio('未視聴', "RADIO5", key='all_viewing_rb1'), sg.Radio('視聴中', "RADIO5", key='all_viewing_rb2'), sg.Radio('視聴済み', "RADIO5", key='all_viewing_rb3', default=True)],
                             ], pad=(13, 13), title='視聴状態'), sg.Frame(layout=[
                                    [sg.Combo((genre_list), default_value='アニメジャンル1', size=(23, 5), key='all_ud_genre_first')],
                                    [sg.Combo((genre_list), default_value='アニメジャンル2', size=(23, 5), key='all_ud_genre_second', pad=(5, 5))]
                                    ], title='ジャンル')],
            [sg.Frame(layout=[
            [sg.Radio('1期', "RADIO6", key='all_what_period1', default=True), sg.Radio('2期', "RADIO6", key='all_what_period2'), sg.Radio('3期', "RADIO6", key='all_what_period3'), sg.Radio('4期', "RADIO6", key='all_what_period4'), sg.Radio('5期以上', "RADIO6", key='all_what_period5'), sg.Radio('短編', "RADIO6", key='all_what_period6'), sg.Radio('長期', "RADIO6", key='all_what_period7'), sg.Radio('映画(劇場版)', "RADIO6", key='all_what_period8')]
            ], pad=(13, 13), title='何期か選択')],
            [sg.Button('実行ボタン', key='all_ud', pad=(235, 13), size=(17,1), button_color=('midnightblue', '#87cefa'))]
        ]

        second_layout_delete = [
            [sg.Frame(layout=[
                [sg.Text('コンボ指定', pad=(5, 5)), sg.Combo(values=(count_n[:-1]), size=(5, 10), change_submits=True, key='column8')],
                [sg.Text('数値指定', size=(9, 0), pad=(5, 5)), sg.Input(key='column_int8', size=(5, 10))],
                [sg.Button('実行', pad=(5, 5), key='delete', button_color=('midnightblue', '#87cefa'))]], pad=(13, 13), title='行の消去')],
        ]

        second_layout2 = [[sg.Table(id_list, headings=alphabet_n2[0:], auto_size_columns=False, vertical_scroll_only=False,
                    header_text_color='#001e43', header_background_color='#a2c2e6',
                    def_col_width=17, num_rows=22, text_color='black',
                    background_color='#ebf6f7', alternating_row_color='#a0d8ef',
                    font=('UD デジタル 教科書体 NK-B', 13))],
                    ]

        second_layout = [
            [sg.TabGroup([
                [sg.Tab('列更新', second_layout_all_update),
                sg.Tab('更新', second_layout_update),
                sg.Tab('消去', second_layout_delete),
                ]]
            ), sg.Frame('IDリスト', second_layout2, pad=(20, 13))],
            [sg.Frame('シート', second_layout1)],
            ]
        
        # def updates(a_number, a_char, number, s_value):
        #     ws0.update_acell(f"{a_number}{number + 2}", s_value)
        #     seat_display[number + 1][a_char] = s_value
        #     second_window['-TableUpdate-'].update(values = seat_display[1:])
        #     sg.popup_quick_message('更新が完了しました')

        # 個別update関数
        def updates(a_number, a_char, number, s_value, text):
            if number == '':
                sg.popup_error('行が選択されていません')
            else:
                ws0.update_acell(f"{a_number}{number + 2}", s_value)
                old_name = seat_display[number + 1][a_char]
                seat_display[number + 1][a_char] = s_value
                second_window['-TableUpdate-'].update(values = seat_display[1:])
                second_window.FindElement(text).Update('')
                sg.popup_quick_message(f'「{old_name}」->「{seat_display[number + 1][a_char]}」に更新が完了しました')

        # 個別ナンバーテキストの更新
        def change_ud_text(texts, updates):
            for i in zip(texts, updates):
                second_window.FindElement(i[0]).Update(i[1])

        second_window = sg.Window('アニメ管理 読み込み', second_layout, no_titlebar=True, grab_anywhere=True)
        while True:
            
            # print(seat_display)
            second_event, second_values = second_window.read()

            # テキストの変換
            ud_text = ['column_text', 'column_text2', 'column_text3', 'column_text4', 'column_text5', 'column_text6', 'column_text7', 'column_int8', 'ud_stars_text', 'all_column_text', 'seasons_text_n']
            combo_column = [second_values['column'], second_values['column2'], second_values['column3'], second_values['column4'], second_values['column5'], second_values['column6'], second_values['column7'], second_values['column8'], second_values['ud_stars_column'], second_values['all_column'], second_values['seasons_column']]
            change_ud_text(ud_text, combo_column)
            
            # print(second_event, second_values)
            # print(second_values)
            # バラバラ更新
            period_number = period(list(second_values.items()), 'ud_what_period') # n期の更新
            genre_number1 = genre(second_values['genre_first_ud'], genre_list) # ジャンル1の更新
            genre_number2 = genre(second_values['genre_second_ud'], genre_list) # ジャンル2の更新
            watching_num = watching_number(list(second_values.items()), 'ud_viewing_rb') # 視聴の更新
            favorite_star = favorite_number(list(second_values.items()), 'ud_star') # お気に入り更新
            seasons_id = seasons_number(list(second_values.items()), 'ud_seasons') # 四季の更新

            # 終了ボタン
            if second_event is None or second_event == 'exit':
                # print('eee')
                break

            # タイトルの更新
            if second_event == 'title_ud':
                updates(alphabet_n[1][0], alphabet_n[1][1], second_values['column'], second_values['title_text'], "column")

            # n期の更新
            if second_event == 'period_ud':
                updates(alphabet_n[2][0], alphabet_n[2][1], second_values['column2'], period_number, 'column2')
            
            # ジャンル1の更新
            if second_event == 'genre_ud1':
                updates(alphabet_n[3][0], alphabet_n[3][1], second_values['column3'], genre_number1, 'column3')
            
            # ジャンル2の更新
            if second_event == 'genre_ud2':
                updates(alphabet_n[4][0], alphabet_n[4][1], second_values['column4'], genre_number2, 'column4')
            
            # 四季の更新
            if second_event == 'seasons_key':
                updates(alphabet_n[5][0], alphabet_n[5][1], second_values['seasons_column'], seasons_id, 'seasons_column')

            # 視聴の更新
            if second_event == 'status_ud':
                updates(alphabet_n[6][0], alphabet_n[6][1], second_values['column5'], watching_num, 'column5')

            # お気に入り更新
            if second_event == 'ud_star_b':
                updates(alphabet_n[7][0], alphabet_n[7][1], second_values['ud_stars_column'], favorite_star, 'ud_stars_column')

            # 公式urlの更新
            if second_event == 'official_url_ud':
                updates(alphabet_n[8][0], alphabet_n[8][1], second_values['column6'], second_values['official_url_text'], 'column6')

            # wikiURLの更新
            if second_event == 'wiki_url_ud':
                updates(alphabet_n[9][0], alphabet_n[9][1], second_values['column7'], second_values['wiki_url_text'], 'column7')
            
            # 全体更新の処理
            if second_event == 'all_ud':
                # 更新する行が選択されていないとpopを表示させる
                if second_values['all_column'] == '':
                    sg.popup_error('行がありません', button_color=('midnightblue', '#87cefa'))
                    continue
                
                # 更新する処理たち
                wiki     = wiki_url(second_values['all_ud_tatal'])
                official2 = official_url(second_values['all_ud_tatal'])
                # writing  = [[hiduke, values['tatal'], period(list(values.items()), 'what_period'), genre(values['genre_first'], genre_list), genre(values['genre_second'], genre_list), 0, watching_number(list(values.items()), 'viewing_rb'), favorite_number(list(values.items()), 'star'), official, wiki]]
                writing2  = [hiduke, second_values['all_ud_tatal'], period(list(second_values.items()), "all_what_period"), genre(second_values['all_ud_genre_first'], genre_list), genre(second_values['all_ud_genre_second'], genre_list), seasons_number(list(second_values.items()), 'all_seasons'), watching_number(list(second_values.items()), "all_viewing_rb"), favorite_number(list(second_values.items()), 'all_ud_star'), official2, wiki]
                # print(writing2)
                # print(f'{alphabet_n[0][0]}{second_values["all_column"] + 2}:{alphabet_n[-1[0]]}{second_values["all_column"] + 2}')
                ds = ws0.range(f'{alphabet_n[0][0]}{second_values["all_column"] + 2}:{alphabet_n[-1][0]}{second_values["all_column"] + 2}')
                for rewrite_location, update_table in zip(ds, writing2):
                    rewrite_location.value = update_table
                ws0.update_cells(ds)
                seat_display[second_values["all_column"] + 1][:] = writing2
                second_window['-TableUpdate-'].update(values = seat_display[1:])
                sg.popup_quick_message('更新が完了しました')

            if second_event == 'delete':
                combo_number = [x for x, i in enumerate(seat_display)]
                # print(len(combo_number))
                # print(combo_number[:-1])
                # print(combo_number[:-2])
                # print(len(count_n))
                try:
                    if second_values['column_int8'].isdecimal() == False:
                        sg.popup_error('数字以外が書かれています', title='エラー')
                        continue
                    if not int(second_values['column_int8']) in combo_number:
                        sg.popup_error('存在しない数字', title='エラー')
                        continue
                except:
                    sg.popup_error('何らかのエラーが発生', title='エラー')
                    continue
                if second_values['column_int8'] != '':
                    no = sg.popup_yes_no(f"本当に{second_values['column_int8']}行目を消去しますか", button_color=('midnightblue', '#87cefa'), title='列の消去')
                    if no == 'No':
                        continue
                    else:
                        ws0.delete_row(int(second_values['column_int8']) + 2)
                        del seat_display[int(second_values['column_int8']) + 1]
                        second_window['-TableUpdate-'].update(values = seat_display[1:])
                        second_window.FindElement('column').Update(values     = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column2').Update(values    = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column3').Update(values    = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column4').Update(values    = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column5').Update(values    = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column6').Update(values    = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column7').Update(values    = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column8').Update(values    = combo_number[:-2], size=(5, 10))
                        second_window.FindElement('all_column').Update(values = combo_number[:-2], size=(5, 5))
                        second_window.FindElement('column_int8').Update('')
                        ws0.add_rows(1)
                        sg.popup_quick_message(f"{second_values['column_int8']}行目を消去しました")
                # elif second_values['column_int8'] == '' or second_values['column8'] == '':
                #     sg.popup_error('失敗')
                #     continue

        second_window.close()

    # col_list = ws0.col_values(1)
    # print(col_list)

window.close()

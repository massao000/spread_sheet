import PySimpleGUI as sg

main_layout = [[sg.Text('Main Window'), sg.OK()]]
main_window = sg.Window('Main', layout=main_layout)


while True:
    main_event, main_value = main_window.read()

    if main_event is None:
        break

    elif main_event == 'OK':
        # サブ画面を開く時に毎回layoutを宣言する
        # エラーが発生せず、何度でもポップアップを開閉できる！
        sub_layout = [[sg.Text('Sub Window'), sg.Cancel()]]
        sub_window = sg.Window('Sub', layout=sub_layout)
        while True:
            sub_event, sub_value = sub_window.read()

            if sub_event is None:
                break

        sub_window.close()

main_window.close()
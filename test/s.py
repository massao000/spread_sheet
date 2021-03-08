import PySimpleGUI as sg
from random import randint as rand

def table_example():
    data = [list(str(rand(0,50)) for i in range(20)) for i in range(5)]
    header_list = list(range(20))
    layout = [[sg.Table(values=data,
                            headings=header_list,
                            max_col_width=25,
                            auto_size_columns=True,
                            justification='r',
                            alternating_row_color='lightblue',
                            display_row_numbers=True,
                            num_rows=min(len(data), 20),
                            key='_TABLE_')]]


    window = sg.Window('Table', layout)
    # here's the patch that will or will not display row numbers
    if window.Element('_TABLE_').DisplayRowNumbers == True:
        window.Element('_TABLE_').QT_TableWidget.verticalHeader().show()
    else:
        window.Element('_TABLE_').QT_TableWidget.verticalHeader().hide()

    event, values = window.Read()

table_example()
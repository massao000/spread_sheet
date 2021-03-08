def te(x, category):
    while True:
        alphabet = [chr(i) for i in range(65, 65 + len(category))]
        for number, i in enumerate(zip(category, alphabet), 1):
            print(number, i)
            print(i[0])
            print(x)
            if i[0] == x:
                return i[1]
            else:
                continue
ll = ['タイトル', 'n期ID', 'ジャンルID１', 'ジャンルID２', '年月日', '四季コード', '視聴コード', '公式ページ', 'wiki']
x = te('ジャンルID１', ll)
print(x)
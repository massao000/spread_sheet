import random
import string


def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]
print(data)
print(headings)
# タイトル 	n期ID	ジャンルID１	ジャンルID２	年月日	四季コード	視聴コード	公式ページ	wiki
# pip install asciichartpy

import asciichartpy


data = [1, 4, 2, 8, 5, 7, 3, 6]
print("ASCII Line Chart")
print(asciichartpy.plot(data, {"height": 10}))


'''output:

ASCII Line Chart
    8.00  ┤
    7.36  ┤  ╭╮
    6.73  ┤  ││╭╮
    6.09  ┤  ││││╭
    5.45  ┤  │││││
    4.82  ┤  │╰╯││
    4.18  ┤╭╮│  ││
    3.55  ┤│││  ││
    2.91  ┤│││  ╰╯
    2.27  ┤│╰╯
    1.64  ┤│
    1.00  ┼╯
'''
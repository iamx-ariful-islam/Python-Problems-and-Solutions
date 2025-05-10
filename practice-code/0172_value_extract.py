def extract_value(data):
    if isinstance(data, dict):
        print('Original data:', data)
        for k, v in data.items():
            print(k, v)
    elif isinstance(data, list):
        print('Original data:', data)
        for x, y in zip(*data):
            print(x, y)
    else:
        print('Original data:', data)
        print(*data)


data1 = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]
data2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
data3 = (1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e')

extract_value(data=data1)
extract_value(data=data2)
extract_value(data=data3)


'''output:

Original data: [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]
1 a
2 b
3 c
4 d
5 e
Original data: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
1 a
2 b
3 c
4 d
5 e
Original data: (1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e')
1 a 2 b 3 c 4 d 5 e
'''
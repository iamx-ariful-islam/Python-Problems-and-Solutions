num = int(input('Enter a valid digit: '))

i = 1
while i <= 10:
    print(f"{num:2} x {i:2} = {num * i:2}")
    i += 1



'''output:

Enter a valid digit: 5
 5 x  1 =  5
 5 x  2 = 10
 5 x  3 = 15
 5 x  4 = 20
 5 x  5 = 25
 5 x  6 = 30
 5 x  7 = 35
 5 x  8 = 40
 5 x  9 = 45
 5 x 10 = 50
'''
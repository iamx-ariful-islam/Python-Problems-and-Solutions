# fun with mathematics
print(f"{1:>11}")
for i in range(1, 6):
    print(f"{'1 '*i:>10}x{' 1'*i}")
    print(' '*(11-i)+str(int('1'*i)*int('1'*i)))


'''output:

          1
        1 x 1
          1
      1 1 x 1 1
         121
    1 1 1 x 1 1 1
        12321
  1 1 1 1 x 1 1 1 1
       1234321
1 1 1 1 1 x 1 1 1 1 1
      123454321
'''
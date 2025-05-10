import math

# find the magic number
num = int(input("Enter a Number: "))

# method #1
digitCount  = int(math.log10(num)) + 1
sumOfDigits = 0

temp = num
while( digitCount > 1):
  sumOfDigits = 0

  while(temp > 0):
    sumOfDigits += temp%10
    temp = temp//10

  temp = sumOfDigits
  digitCount = int(math.log10(sumOfDigits)) + 1
   
if sumOfDigits==1: print("Magic number")
else: print("Not a magic number")


# method #2
n = str(num)
while len(n) > 1:
    li = [int(x) for x in n]
    n = str(sum(li))

if int(n)==1: print('Magic number')
else: print('Not a magic number')


'''output:

Enter a Number: 100
Magic number
Magic number

Enter a Number: 202
Not a magic number
Not a magic number
'''
# pip install word2number

from word2number import w2n


txt1 = 'two million three thousand nine hundred and eighty four'
txt2 = 'POINT ZERO ONE'
txt3 = 'TWO HUNDRED EIGHTY FOUR'
txt4 = 'two point three' # print point value
txt5 = 'one hundred thirty-five'
txt6 = '123'

print(w2n.word_to_num(txt1))
print(w2n.word_to_num(txt2))
print(w2n.word_to_num(txt3))
print(w2n.word_to_num(txt4))
print(w2n.word_to_num(txt5))
print(w2n.word_to_num(txt6))


''' output:

2003984
0.01
284
2.3
135
123
'''
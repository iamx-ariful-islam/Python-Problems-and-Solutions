# set defaults values
data = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
        'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000,'million':1000000,'billion':1000000000,'trillion':1000000000000,'quadrillion':1000000000000000,
        'quintillion':1000000000000000000,'sextillion':1000000000000000000000,'septillion':1000000000000000000000000,'octillion':1000000000000000000000000000,'nonillion':1000000000000000000000000000000,'decillion':1000000000000000000000000000000000,
        'undecillion':1000000000000000000000000000000000000,'duodecillion':1000000000000000000000000000000000000000,'tredecillion':1000000000000000000000000000000000000000000,'quattuordecillion':1000000000000000000000000000000000000000000000,
        'quindecillion':1000000000000000000000000000000000000000000000000,'sexdecillion':1000000000000000000000000000000000000000000000000000,'septendecillion':1000000000000000000000000000000000000000000000000000000,'octodecillion':1000000000000000000000000000000000000000000000000000000000,
        'novemdecillion':1000000000000000000000000000000000000000000000000000000000000,'vigintillion':1000000000000000000000000000000000000000000000000000000000000000}

# find words from numbers
def find_nums(words):
    total = 0
    value = 0
    for word in words:
        if word.isdigit():
            value += int(word)
        elif word in data:
            if word == "hundred":
                value *= data[word]
            elif word in ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion']:
                total += value * data[word]
                value = 0
            else:
                value += data[word]
    return total + value

# convert word to number
def WordsToNum(word):
    words  = word.lower().split()
    wL = len(words)
    pindex = wL

    try: pindex = words.index('point')
    except: pass
    total = find_nums(words[:pindex])

    if wL > pindex:
        x = words[pindex+1:]
        x.extend(['zero', 'zero']) if len(x) < 1 else x.append('zero')
        total += (data[x[0]]*10 + data[x[1]])/100
    return total
        

if __name__ == '__main__':
    x = 'one million two hundred thirty four thousand five hundred sixty seven point two six'
    print(WordsToNum(x))


'''output:

1234567.26
'''
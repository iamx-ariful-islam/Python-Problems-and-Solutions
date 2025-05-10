# set defaults values
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
powers = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion']
    
# find words from numbers
def find_words(x):
    if x < 0: return 'minus ' + find_words(abs(x))
    if x < 20: return ones[x]
    if x < 100: return tens[x // 10] + ('' if x % 10 == 0 else ' ' + ones[x % 10])
    if x < 1000:
        return ones[x // 100] + ' hundred' + ('' if x % 100 == 0 else ' ' + find_words(x % 100))
    words = []
    for i in range(len(powers)):
        if x == 0: break
        triplet = x % 1000
        if triplet != 0:
            words.append(find_words(triplet) + ' ' + powers[i])
        x //= 1000
    return ' '.join(reversed(words))

# convert numbers to words
def NumToWords(x, prefix='', suffix=''):
    d = []
    if type(x)==int: pass
    elif type(x)==float:
        x, y = str(round(x, 2)).split('.')
        d = [int(i) for i in y]
    else: return

    in_words = find_words(int(x))

    if sum(d) > 0:
        if len(d) == 1: d.append(0)
        in_words += 'point ' + ones[d[0]] + ' ' + ones[d[1]]
    else:
        try: d[0] == 0; in_words += 'point ' + ones[0]
        except: pass
    return (prefix + ' ' + in_words + ' ' + suffix).strip()


if __name__ == '__main__':
    x = 1234567.26
    print(NumToWords(x))


'''output:

one million two hundred thirty four thousand five hundred sixty seven point two six
'''
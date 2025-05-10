import time

# print iterations progress
def printProgressBar (iteration, total): # length = 100
    prefix = 'Progress'
    suffix = 'Complete'
    length = 50
    """
    call in a loop to create terminal progress bar
    -params:
        iteration   - required  : current iteration (int)
        total       - required  : total iterations (int)
        prefix      - optional  : prefix string (str)
        suffix      - optional  : suffix string (str)
        decimals    - optional  : positive number of decimals in percent complete (int)
        length      - optional  : character length of bar (int)
        fill        - optional  : bar fill character (str)
        printEnd    - optional  : end character (e.g. "\r", "\r\n") (str)
    """
    percent  = "{0:.1f}".format(100 * (iteration / float(total)))
    flength  = int(length * iteration // total) # length = 50
    bar_icon = '█' * flength + '░' * (length - flength)
    
    print('\r%s |%s| [%s%%] %s' % (prefix, bar_icon, percent, suffix), end = '\r')
    # print(f'\r{prefix} |{bar}| [{percent}%] {suffix}\r')
    # print newline on complete
    if iteration == total: 
        print()

# a list of items
chunk_size = 259.19
items = list(range(0, 57))
l = len(items)

# initial call to print 0% progress
printProgressBar(0, l)
for i, item in enumerate(items):
    # do stuff...
    time.sleep(0.1)
    # update progress bar
    printProgressBar(i + 1, l)


'''output:

Progress |██████████████████████████████████████████████████| [100.0%] Complete
'''
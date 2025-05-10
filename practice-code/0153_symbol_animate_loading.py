import time


'''animation = "\u22F1 \u22EE \u22EF \u22F0 "

idx = 0
while idx <= 50:
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)'''

mText = ["[        ]", "[●       ]", "[●●      ]", "[●●●     ]", "[●●●●    ]", "[●●●●●   ]", "[●●●●●●  ]", "[●●●●●●● ]", "[●●●●●●●●]",
             "[ ●●●●●●●]", "[  ●●●●●●]", "[   ●●●●●]", "[    ●●●●]", "[     ●●●]", "[      ●●]", "[       ●]", "[        ]", "[        ]"]

notcomplete = True

i = 0
while True:
    print('loading...' + mText[i % len(mText)], end='\r')
    time.sleep(.1)
    i += 1
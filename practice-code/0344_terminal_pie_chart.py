data   = [5, 3, 2]
labels = ["A","B","C"]
total  = sum(data)

for i,v in enumerate(data):
    percent = v/total*100
    print(f"{labels[i]}: {'#' * int(percent/5)} {percent:.1f}%")
    
    
'''output:

A: ########## 50.0%
B: ###### 30.0%
C: #### 20.0%
'''
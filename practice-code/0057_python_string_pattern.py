s = 'python'
p = [s[:i] for i in range(1, len(s)+1)]
for i in p:
    print(f'{i*(len(i)):^40}')


'''output:

                   p
                  pypy
               pytpytpyt
            pythpythpythpyth
       pythopythopythopythopytho
  pythonpythonpythonpythonpythonpython
'''
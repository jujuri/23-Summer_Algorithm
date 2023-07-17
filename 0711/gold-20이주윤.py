import sys
input = sys.stdin.readline

dictionary = []
puzzle = []

inp = ''
while True:
    inp = input().strip()
    if inp == '-':
        break
    dictionary.append(inp)
    
while True:
    inp = input().strip()
    if inp == '#':
        break
    puzzle.append(inp)
        
for i in puzzle:
    alphabet = dict()
    for j in i:
        if j in alphabet:
            alphabet[j] += 1
        else:
            alphabet[j] = 1
            
    check = dict()
    for j in alphabet:
        check[j] = 0
        
    for j in dictionary:
        tmp = alphabet.copy()
        flag = False
        
        for k in j:
            if tmp.get(k) == None or tmp[k] == 0:
                flag = True
                break
            tmp[k] -= 1
        if not flag:
            alphabet_set = set(j)
            for k in alphabet_set:
                check[k] += 1

    
    maximum = max(check.values())
    minimum = min(check.values())
    check = check.items()
    max_char = ''
    min_char = ''
   
    for j in check:
        if j[1] == maximum:
            max_char += j[0]
        if j[1] == minimum:
            min_char += j[0]
            
    max_char = sorted(max_char)
    min_char = sorted(min_char)
    maxchar = ''.join(max_char)
    minchar = ''.join(min_char)
    print(minchar + " " + str(minimum) + " " + maxchar + " " + str(maximum))

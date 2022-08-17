gram = ['E->E+T', 'E->T', 'T->T*F', 'T->F', 'F->(E)', 'F->i']
encoding = {'State': 0, '+': 1, '*':2, '(':3, ')':4, 'i':5, '$':6, 'E':7, 'T':8, 'F':9, 't':10, 'e':11}
table = [['0','#','#','s4','#','s5','#','1','2','3'], 
['1','s6', '#', '#', '#', '#', 'Accept', '#', '#', '#'],
['2', 'r2', 's7', '#', 'r2', '#', 'r2', '#', '#', '#'],
['3', 'r4', 'r4', '#', 'r4', '#', 'r4', '#', '#', '#'],
['4', '#', '#', 's4', '#', 's5', '#', '8', '2', '3'],
['5', 'r6', 'r6', '#', 'r6', '#', 'r6', '#', '#', '#'],
['6', '#', '#', 's4', '#', 's5', '#', '#', '9', '3'],
['7', '#', '#', 's4', '#', 's5', '#', '#', '#', 't'],
['8', 's6', '#', '#', 'se', '#', '#', '#', '#', '#'],
['9', 'r1', 's7', '#', 'r1', '#', 'r1', '#', '#', '#'],
['t', 'r3', 'r3', '#', 'r3', '#', 'r3', '#', '#', '#'], #t=10
['e', 'r5', 'r5', '#', 'r5', '#', 'r5', '#', '#', '#'], #e=11
]

input = "i+i*+i$"
stk="$0"
print("\nSTACK\t  |  INPUT BUFFER | ACTION \n")
i=0
while i<len(input):
    print(stk, end="\t\t")
    print(input[i:],end="\t\t")
    if stk[-1]=="t":
        action=table[10][encoding[input[i]]]
    elif stk[-1]=="l":
        action=table[11][encoding[input[i]]]
    else:
        action=table[int(stk[-1])][encoding[input[i]]]
    if action == "Accept":
        print("ACCEPT")
        exit(0)
    elif action[0]=='s':
        stk+=input[i]+action[1]
        i+=1
        print("Shift"+action[1])
    elif action[0]=="r":
        curGram = gram[int(action[1])-1]
        stk = stk[::-1][len(curGram[3:])*2:][::1]
        stk+=curGram[0]
        stk+=table[int(stk[-2])][encoding[stk[-1]]]
        print("Reduce"+action[1]+" "+curGram)
    elif action[0] == "#":
        print("REJECT")
        exit(0)
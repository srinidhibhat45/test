
stk = "$S"

input="cdd$"

encode = {'S':0,'C':1,'c':0,'d':1,'$':2}

table = [["S->CC","0"],["C->cC","C->d","0"]]

i=0
while i<len(input):
    print(stk,end="\t\t")
    print(input[i:],end="\t\t")
    if stk[-1] == input[i]=="$":
        print("Accept",end="\n\n")
        exit(0)
    elif stk[-1] == input[i] != "$":
        print(f"Pop {stk[-1]}",end="\n")
        stk = stk[:-1]
        i+=1
    else:
        entry = table[encode[stk[-1]]][encode[input[i]]]
        if entry == '0':
            print("Reject",end="\n\n")
            exit(0)
        else:
            stk = stk[:-1] + entry[3:][::-1]
            print(f"Push {entry}",end="\n")
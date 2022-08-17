stk="$"
G = { 
    "S" : ["S+S","S*S","a"],
}

input = "a+a*a$"

def chk():
    global stk
    i=1
    while i<len(stk):
        grams=[]
        for prod_list in G.values():
            for prod in prod_list:
                grams.append(prod)
        if stk[i:] in grams:
            for key in G:
                value = G[key]
                if stk[i:] in value:
                    stk = stk.replace(stk[i:],key)
                    return stk
        i+=1
    return None

a=0
while a<len(input):
    print(stk,end="\t\t")
    print(input[a:],end="\t\t")

    if not chk():
        if input[a]=='$':
            if stk[-1]=='S':
                print("Accepted",end="\n\n")
            else:
                print("Invalid",end="\n\n")
        else:
            print("Shift")
        stk+=input[a]
        a+=1
    else:
        print("Reduce")
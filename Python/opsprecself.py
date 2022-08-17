arr = [
        ['>','<','<','>','<','>'],
        ['>','>','<','>','<','>'],
        ['<','<','<','=','<','999'],
        ['>','>','999','>','999','>'],
        ['>','>','999','>','999','>'],
        ['<','<','<','999','<','999'],
]
stack = [5]
input='a + a * a $'
temp=[]

for char in input.split():
    if (char=='+'):
        temp.append(0)
    elif (char=='*'):
        temp.append(1)
    elif (char=='('):
        temp.append(2)
    elif (char==')'):
        temp.append(3)
    elif (char=='a'):
        temp.append(4)
    elif (char=='$'):
        temp.append(5)

i=0
def convert(newarr):
    sec=""
    x=0
    while x<len(newarr):
        if(newarr[x]==0):
            sec+='+'
        if(newarr[x]==1):
            sec+='*'
        if(newarr[x]==2):
            sec+='('
        if(newarr[x]==3):
            sec+=')'
        if(newarr[x]==4):
            sec+='a'
        if(newarr[x]==5):
            sec+='$'
        x+=1
    return sec

i=0
while(i<len(temp)):
    print(convert(stack),end="\t\t")
    print(convert(temp[i:]),end="\t\t")
    if(arr[stack[-1]][temp[i]]=='<' or arr[stack[-1]][temp[i]]=='='):
        stack.append(temp[i])
        print("Push")
    elif(arr[stack[-1]][temp[i]]=='>'):
        stack.pop()
        i-=1
        print("Pop")
    else:
        if(temp[i]==5):
            break
        print("Reject")
        exit(0)
    i+=1
print("Accept")
    
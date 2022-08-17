arr = [
        ['>','<','<','>','<','>'],
        ['>','>','<','>','<','>'],
        ['<','<','<','+','<','999'],
        ['>','>','999','>','999','>'],
        ['>','>','999','>','999','>'],
        ['<','<','<','999','<','999'],
]

stack = [5]

input = 'a + a * a $'
temp = []

for char in input.split():
    if(char == '+'):
        temp.append(0)
    if(char == '*'):
        temp.append(1)    
    if(char == '('):
        temp.append(2)
    if(char == ')'):
        temp.append(3)
    if(char == 'a'):
        temp.append(4)
    if(char == '$'):
        temp.append(5)

def convert(newar):
    sec=""
    x=0
    while x<len(newar):
        if(newar[x]==0):
            sec+='+'
        elif(newar[x]==1):
            sec+='*'
        elif(newar[x]==2):
            sec+='('
        elif(newar[x]==3):
            sec+=')'
        elif(newar[x]==4):
            sec+='a'
        elif(newar[x]==5):
            sec+='$'
        x+=1
    return sec

i=0
print("Stack \t | Input Buffer \t | Action \n")
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
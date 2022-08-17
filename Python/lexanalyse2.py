import re

preprocessor = ['#']
headerFile = ['stdio.h','iostream.h','math.h']
operators = ['+','-','*','/','%']
seperators = [',',';']
punctuation = ['>','<','{','}','[',']','(',')']
keyword = ['return','int','void','include']
content = "# include < stdio.h > int main { int a , b ; a = 1 ; b = 2 ; return ( a + b ) ; }"

splitC = content.split()
size = len(splitC)
i=0
print("Token\t\t | \tLexeme")
for i in range(0,size):
    if splitC[i] in preprocessor:
        print(splitC[i],"\t\t | \tPreprocessor")
        continue
    elif splitC[i] in headerFile:
        print(splitC[i],"\t | \tHeader File")
        continue
    elif splitC[i] in operators:
        print(splitC[i],"\t\t | \tOperator")
        continue
    elif splitC[i] in seperators:
        print(splitC[i],"\t\t | \tSeperator")
        continue
    elif splitC[i] in punctuation:
        print(splitC[i],"\t\t | \tPunctuation")
        continue
    elif splitC[i] in keyword:
        print(splitC[i],"\t | \tKeyword")
        continue
    elif re.match('^[+-]?[0-9]+$',splitC[i]):
        print(splitC[i],"\t\t | \tConstant")
        continue
    elif re.match('^[a-zA-Z_]+$',splitC[i]):
        print(splitC[i],"\t\t | \tVariable")
        continue

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
print('Token \t\t| Lexemes \n')
for i in range(0,size):
    if splitC[i] in preprocessor:
        print('Preprocessor \t|',splitC[i])
        continue
    if splitC[i] in headerFile:
        print('Header File \t|',splitC[i])
        continue
    if splitC[i] in operators:
        print('Operators \t|',splitC[i])
        continue
    if splitC[i] in seperators:
        print('Seperator \t|',splitC[i])
        continue
    if splitC[i] in punctuation:
        print('Punctuation \t|',splitC[i])
        continue
    if splitC[i] in keyword:
        print('Keyword \t|',splitC[i])
        continue
    if re.match('^[-+]?[0-9]+$',splitC[i]):
        print('Constant \t|',splitC[i])
        continue
    if re.match('^[a-zA-Z_]+$',splitC[i]):
        print('Variable \t|',splitC[i])
        continue

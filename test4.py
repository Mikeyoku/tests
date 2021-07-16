var1 = str(input())
var2 = str(input())

l1 = len(var1)
l2 = len(var2)

if var1 == var2:
    print('OK')
elif var2.find('*') != -1:
    print('OK')
else:
    print("KO")

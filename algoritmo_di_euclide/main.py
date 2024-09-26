print("Inserisci M")
m = int(input())
print("Inserisci N")
n = int(input())

x = m
y = n

while( x != 0 and y != 0 ):
    r = x/y
    print(r)
    if( r == 0):
        print("The answer is ", y)
        break
    else:
        x = y
        y = r
else:
    print("trival answer or impossibile to calculate")

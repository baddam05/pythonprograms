#checking perfect number
n = 24
f = 0

for i in range(1, n // 2 + 1):
    if n % i == 0:
        f = f + i
if f == n:
    print(n, ":is  a perfect number")
else:
    print(n, ":is not a perfect number")
#approach 1 in between numbers
a = 1#int(input("Enter first number ::"))
b = 10000# int(input("Enter second number ::"))
print("perfect numbers in the given range are : ", end='')
while a < b:
    fac = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            fac = fac + i
    if fac == a:
        print(a, end=' ')
    a = a + 1
#approach 2
n = 1000
y= []
for x in range(1,n+1):
    f = 0
    for i in range(1, x):
        if x % i == 0:
            f = f + i
    if f == x:
        y.append(x)
        print(x, ":is a perfect number")

print( y,"perfect numbers from 1-1000 are:")





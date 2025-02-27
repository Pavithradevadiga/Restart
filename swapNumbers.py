print('Swap Numbers')

a,b = map(int,input("Please enter 2 numbers: ").split())
print(f"{a} = a, {b} = b")

a = a + b
b = a - b
a = a - b

print(f"{a} = a, {b} = b")
import math

print('Print if a number is prime or not')

n = int(input("Enter your number "))
number = "PRIME"
midNumber = math.floor(n/2)

for i in range(2,midNumber):
    if n % i == 0:
        number = "NOT PRIME"
        break
    else:
        pass

if number == "NOT PRIME":
    print(f"{n} is not prime number")
else:
    print(f"{n} is a prime number")
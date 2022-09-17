#Exercise 1:
a = int(input("Enter your number: "))
b = min(a, 0)

if a == 0:
    print("You entered 0")
else:
    print(b or "Number is > 0")

#Exercise 2:
c = int(input("Enter your number: "))
d = 20 - c

if d == 0:
    print("You entered 20")
else:
    print(max(0, d) or "Number is bigger than 20")
    print(max(0, d) and "Number is less than 20")

#Exercise 3:
e = int(input("Enter your number: "))
print(e and "Not 0")

#Exercise 4:
f = int(input("Enter your number: "))
g = f % 2
print(f % 2 or "Number is Even ")
print(f % 2 and "Number is Odd")

#Exercise 5:
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

print(f'Largest number is {max(num1, num2, num3)}')


#Exercise 1:
a = "123"
b = int(a)

#Exercise 2:
c = 123
d = float(c)

#Exercise 3:
e = 12.345
f = int(e)

#Exercise 4:
ccnum = input("Enter your credit card number (without spaces): ")
print("Last 4 digits: ", ccnum[12:16])

#Exercise 5:
tdnum = int(input("\nEnter your 3-digit number: "))
d1 = tdnum // 100
d2 = (tdnum - d1 * 100) // 10
d3 = tdnum - d1 * 100 - d2 * 10
print("Sum of three digits of your number: ", d1 + d2 + d3)

#Exercise 6:
import math

sA = int(input("\nEnter side A: "))
sB = int(input("Enter side B: "))
sC = int(input("Enter side C: "))

p = (sA + sB + sC) / 2

S = math.sqrt(p * (p - sA) * (p - sB) * (p - sC)) # или, если без модуля math - возвести все в степень 0.5 для получения корня

print("Area of your triangle: ", S)

#Exercise 7:
num = input("\nEnter your number: ")
num_str = list(num)
num_int = map(int, num_str)
s1 = sum(num_int)
print("Sum of digits in your number: ", s1)

#Exercise 8:
numb = input("\nEnter your number: ")
print("Length of your number: ", len(numb))

#Exercise 9:
num9 = input("\nEnter your number: ")
print("Reverse number: ", num9[::-1])
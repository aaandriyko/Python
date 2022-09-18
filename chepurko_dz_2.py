#Exercise 1: str to int
a = "123"
b = int(a)



#Exercise 2: int to float
c = 123
d = float(c)



#Exercise 3: float to int
e = 12.345
f = int(e)



#Exercise 4: Detect last 4 digits of a credit card
ccnum = input("Enter your credit card number (without spaces): ")
print("Last 4 digits: ", ccnum[12:16])



#Exercise 5: Calculate the sum of digits in a 3-digit number
tdnum = int(input("\nEnter your 3-digit number: "))
d1 = tdnum // 100
d2 = (tdnum - d1 * 100) // 10
d3 = tdnum - d1 * 100 - d2 * 10
print("Sum of three digits of your number: ", d1 + d2 + d3)



#Exercise 6: Area of a triangle if its sides are known
import math

sA = int(input("\nEnter side A: "))
sB = int(input("Enter side B: "))
sC = int(input("Enter side C: "))

p = (sA + sB + sC) / 2

S = math.sqrt(p * (p - sA) * (p - sB) * (p - sC)) # ** 0.5 in case we don't import math module

print("Area of your triangle: ", S)



#Exercise 7: Calculate the sum of digits of a number
num = input("\nEnter your number: ")
num_str = list(num)
num_int = map(int, num_str)
s1 = sum(num_int)
print("Sum of digits in your number: ", s1)



#Exercise 8: Determine the number of digits in a number
numb = input("\nEnter your number: ")
print("Length of your number: ", len(numb))



#Exercise 9: Print the digits in reverse order
num9 = input("\nEnter your number: ")
print("Reverse number: ", num9[::-1])

#Exercise 1: Print the number entered by user only if it is negative
a = int(input("Enter your number: "))
b = min(a, 0)

if a:
    print(b or "Number is > 0")
else:
    print("You entered 0")

    
    
#Exercise 2: Check if the value is less than 20 or not
c = int(input("Enter your number: "))
d = 20 - c

if d == 0:
    print("You entered 20")
else:
    print(max(0, d) or "Number is bigger than 20")
    print(max(0, d) and "Number is less than 20")

    
    
#Exercise 3: Check if a given number 0 or not
e = int(input("Enter your number: "))
print(e and "Not 0")



#Exercise 4: Check if a given number Even or Odd
f = int(input("Enter your number: "))
g = f % 2
print(f % 2 or "Number is Even ")
print(f % 2 and "Number is Odd")



#Exercise 5: Find largest number among three given numbers entered by user
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

print(f'Largest number is {max(num1, num2, num3)}')


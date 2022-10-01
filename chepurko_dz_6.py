#Exercise 1: Write a script that displays all numbers in the range from 1 to 100 that are multiples of 7
for i in range(1, 101):
    if not i % 7:
        print(i)
    i += 1
 
#Or

i = 0
while i < 100:
    print(i)
    i += 7

#Or

for i in range(0, 100, 7):
    print(i)



#Exercise 2: Write a script to calculate the factorial of n using a loop. n is entered from the keyboard
n = int(input('Enter your number: '))
m = 1
if n > 0:
    for n1 in range(1, n + 1):
        m = m * n1
    print(f'{n}! = {m}')
elif not n:
    print('0! = 1')
else:
    print('You entered not a natural number')

#Or

n - int(input('n = '))
res = 1
for i in range(2, n + 1):
    res *+ i

print(res)



#Exercise 3: Multiplication table by 5
number = int(input('Enter the last number in the table: '))
for n2 in range(1, number + 1):
    n2 = n2 * 5
    print(f'{n2 // 5} * 5 = {n2}')

#Or

for i in range(1, 11):
    print(f'5 x {i} = {5 * i}')
    
#Or
for j in range(1, 11):
    for i in range(1, 11):
        print(f'{j} x {i} = {j * i}')
    print('*' * 20)



#Exercise 4: Display a rectangle that consists of '*'.
#Hight and width are entered from keyboard
hight = int(input("Enter hight: "))
width = int(input("Enter width: "))

a = '*' * width
print(a)

for a1 in range(1, hight - 1):
    print('*', ' ' * (width - 4), '*')

print(a)

#Or

n, m = 5, 7
res = '*' * m + '\n'
res += (n - 2) * f'*{' ' * (m - 2)}*\n'
res += '*' * m + '\n'
print(res)



#Exercise 5: Count odd numbers in list
c = [0, 5, 2, 4, 7, 1, 3, 19]
print('Your list: ', c)

for c1 in range(len(c)):
    c[c1] = c[c1] % 2
    c1 += c1
# print(c)
res = c.count(1)
print('Number of odd numbers in your list: ', res)



#Exercise 6: Create a list of random numbers (size = 4 elements).
#Create a second list twice the size of the first list, where the 1st 4 elemenst
#must be equal to the elements of 1st list and the rest of the elements
#must be double the values of the 1st
import random
d = []
for d1 in range(4):
    d.append(int(random.uniform(1, 9)))
    d1 += 1

e = d.copy()
for e1 in range(len(e)):
    e[e1] = e[e1] * 2
    e1 += 1
print('List 1: ', d, '\nList 2:', e, '\nResult: ', d + e)



#Exercise 7: Average salary form 12 salaries
f = []
for f1 in range(12):
    f.append(int(random.uniform(15000, 20000)))
    f1 += 1
print('List of salaries in UAH: ', f)

e = sum(f)
print('Average salary: ', e // 12)



#Exercise 8: Display the matrix and the sum of it's elements
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for el in range(len(matrix)):
    print(matrix[el])
    el += 1

m2 = [*matrix[0], *matrix[1], *matrix[2], *matrix[3]] #Не додумался, как это сделать через цикл
print(f'Sum = {sum(m2)}')



#Exercise 9: Mirror flip the list
l1 = [7, 2, 9, 4]
print(l1, '->', l1[::-1])



#Exercise 10: Prime numbers
for j in range(1, 101):
    if j > 1:
        for k in range(2, j):
            if (j % k) == 0:
                break
        else:
            print(j)



#Exercise 11: Hourglass
height_11 = int(input('Enter height of hourglass: '))

for i_11 in range(height_11, 0, -1):
    for j_11 in range(height_11 - 1):
        print(' ', end='')
    for j_11 in range(1, 2 * i_11):
        print('*', end='')
    print()

for i_11 in range(2, height_11 + 1):
    for j_11 in range(height_11 - i_11):
        print(' ', end='')
    for j_11 in range(1, 2 * i_11):
        print('*', end='')
    print()

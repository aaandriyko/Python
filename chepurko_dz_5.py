#Exercise 1: Lucky number
l_num = input('Enter your number: ')

x = list(l_num)
middle_num = len(x) // 2

res = x.pop(middle_num) if len(x) % 2 else x

left = sum(list(map(int, x[:middle_num])))
right = sum(list(map(int, x[middle_num:])))

res1 = 'You\'ve got a lucky one' if left == right else 'Maybe another time...'
print(res1)



#Exercise 2: Palindrome or not
inp_num = input('Enter your number: ')

x = list(inp_num)
divider = int(len(x) / 2)
x1 = x.pop(divider) if len(x) % 2 else x
l_part = list(map(int, x[:divider]))
r_part = list(map(int, x[divider:]))
r_part.reverse()

res1 = 'You\'ve got a palindrome!' if l_part == r_part else 'Unfortunately that\'s not a palindrome :\'('
print(res1)



#Exercise 3: Does the point belong to the circle
x1, y1 = int(input('Enter x: ')), int(input('Enter y: '))
r_sqr = x1 ** 2 + y1 ** 2
R = 4
res2 = 'You\'re inside the circle' if r_sqr <= R ** 2 else 'You\'re outside the circle'
print(res2)
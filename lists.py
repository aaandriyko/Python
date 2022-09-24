#----------------------------------------------------------

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# print(x[1][2])
#
# x[0], x[3] = x[3], x[0]

#----------------------------------------------------------

# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# y = x.copy()
#
# print(x)
# print(y)
#
# print(id(x))
# print(id(y))
#
# y[0][0] = 100
# print(x)

#----------------------------------------------------------

# x = [1, 2, 3, 4, 1, 2, 3]
#
# x.remove(2) #Удаляет элемент
# print(x)
#
# item = x.pop() #Удаляет последний
# print(item) #Выводит его
# print(x)
#
# x.insert(2, 100) #Вставляет на 2 позицию элемент 100

#----------------------------------------------------------

# x = [1, 3, 3, 5, 1, 2, 3, 10, 20, 30]
# print(x[::2]) #Парные
# print(x[1::2]) #Непарные
# print(x[::-1]) #Реверс

#----------------------------------------------------------


#Exercise 1: Reverse a list
list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

#Or

list1.reverse()
print(list1)



#Exercise 2: Concatenate two lists index-wise
list2 = ['M', 'na', 'i', 'Ke']
list3 = ['y', 'me', 's', 'lly']

list4 = [list2[0] + list3[0], list2[1] + list3[1], list2[2] + list3[2], list2[3] + list3[3]]
print(list4)

#Or

for i in range(4):
    list5 = str([list2[i] + list3[i]])
    i += 1
    print(list5)

#Or
list6 = [i + j for i, j in zip(list2, list3)]
print(list6)



#Exercise 3: Turn every item of a list into its square
number_s = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(number_s)):
    number_s[i] = number_s[i] ** 2
    i += 1
print(number_s)

#Or
number_s2 = [1, 2, 3, 4, 5, 6, 7, 8]
res = []

for i in number_s2:
    res.append(i * i)
print(res)

#Or

number_s3 = [1, 2, 3, 4, 5, 6, 7]
res2 = [d * d for d in number_s3]
print(res2)



#Exercise 4: Concatenate two lists crosswise
list7 = ['Hello, ', 'Goodbye, ', 'How are you, ']
list8 = ['Andrii', 'John', 'Sarah']

res3 = [x + y for x in list7 for y in list8]
print(res)



#Exercise 5: Iterate both lists simultaneously (list9 in orig order, list10 in reverse order)
list9 = [10, 20, 30, 40]
list10 = [100, 200, 300, 400]

for f, g in zip(list9, list10[::-1]):
    print(f, g)



#Exercise 6: Remove empty strings from the list of strings
list11 = ['Mike', '', 'Emma', 'Kelly', '', '', 'Brad']
list12 = list(filter(None, list11))
print(list12)



#Exercise 7: Add new item to list after a specified item
list13 = [1, 2, [30, 40, [500, 600], 70], 8, 9]
         #0  1  2|0  2|1 2|2|0 2|2|1 2|3  3   4
list13[2][2].append(65)
print(list13)



#Exercise 8: Extend nested list by adding the sublist
list14 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
list15 = ['h', 'i', 'j']

list14[2][1][2].extend(list15)
print(list14)



#Exercise 9: Replace list's item with new value if found. Only update the 1st item
list16 = [5, 10, 15, 20, 25, 50, 20]
index = list16.index(20)

list16[index] = 200
print(list16)



#Exercise 10: Remove all occuuences of a specific item from a list
list1 = [5, 20, 15, 20, 25, 50, 20]

def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res4 = remove_value(list1, 20)
print(res4)
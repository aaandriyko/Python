#Exercise 1: Count all 'b' letters in a str
# text = input("Enter text: ")
# c = text.count('b')
# print(c)
#


#Exercise 2: Is name valid or not
# name = input("Enter name:")
# no_numb = name.isalpha()
# cap = name[0].isupper()
# low = name[1:].islower()
#
# res1 = f'Nice to meet you, {name}' if no_numb and cap and low else 'Not a valid name:\n' \
#                                                                    '-No numbers allowed;\n' \
#                                                                    '-First letter is uppercase;\n' \
#                                                                    '-Other letters are lowercase.'
# print(res1)



#Exercise 3: Display a sum of all ascii - codes in a string
# str_ing = input("Enter your string: ")
# count = 0
#
# for item in str_ing:
#     print(ord(item))
#     count += ord(item)
#
# print('Sum = ', count)



#Exercise 4:
# import math
# PI = str(math.pi)[2:]
#
# for item2 in range(2, 12):
#     print(f'3.{PI[:int(item2)]}')



#Exercise 5: Find the longest word
# phrase = input('Enter your phrase: ')
# phrase_list = phrase.split()
# max_el = phrase_list[0]
# for x in phrase_list:
#     if len(x) > len(max_el):
#         max_el = x
#
# print('Longest word is:', max_el)



#Exercise 1*: Display a word in a phrase with that word repeated (catcatcat = cat)
# word = input("Enter repeated word: ")
# for i1 in range(len(word)):
#     for j1 in range(i1 + 1, len(word)):
#         if word[i1] == word[j1]:
#             word = word[:j1] + '0' + word[j1 + 1:]
#
# res2 = word.replace('0', '')
# print('Original word:', res2)



#Exercise 2*: Delete all HTML-tags from text
import re
text = input("Enter text with HTML-tags: ")
clean = re.compile('<.*?>')
text = re.sub(clean, '', text)
while '  ' in text:
    text = text.replace('  ', ' ')
print("Text without tags: ", text)


#Exercise 1: radians into degrees
# rad = int(input("Enter value in radians: "))
# PI = 3.14159
# print(f'Value in degrees: {rad * 180 / PI}')

#Exercise 2: decimal into binary
# decnum = int(input("Enter your dec number: "))
# print(f"Dec: {decnum}, Bin: {bin(decnum)}")

#Exercise 3: Count the number of vowels in a str
# word = input("Print your word: ")
# vow = 0
#
# for i in word:
#     if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i' or i=='A' or i=='E' or i=='O' or i=='U' or i=='I'):
#         vow = vow+1
# print("Number of vowels: ", vow)

#Exercise 4: Hide the credit card number
# ccnum = input("Enter your credit card num: ")
# strlen = len(ccnum)
# masked = strlen - 4
# slimstr = ccnum[masked:]
# print("*" * masked + slimstr)
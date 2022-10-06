#Exercise 1: Name of the day by number
weekdays = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
for days in weekdays:
    print(weekdays[days])



#Exercise 2: Describe a cat
animal = {
    'family': 'felidae',
    'genus': 'cat',
    'gender': 'male',
    'color': 'grey and white',
    'age': 1.7,
    'name': 'Vasyl'
}
print(animal.get('color'))



#Exercise 3: Count letters in a str
text = input('text= ')

res = {}

for char in text:
    if not res.get(char):
        res[char] = text.count(char)

print(res)

#Or

# text = input('text= ')
#
# res = {}
#
# for char in text:
#     if not res.get(char):
#         res[char] = 1
#     else:
#         res[char] += 1
#
# print(res)



#Exercise 4: Words to numbers (currency)
import re
money_num = input('Enter the amount of money:')
x = re.split('[,|.]', money_num)
dollars = x[0]
cents = x[1]

money_units = {
    1: ('zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'),
    10: ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'),
    20: ('zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
}
cents_out = 0
if len(cents) == 1:     #123,4 -> forty cents and not four cents
    cents_out = money_units[20][int(cents)]
elif cents[1] == '0':   #123,40 ->forty cents and not forty zero cents
    cents_out = money_units[20][int(cents[0])]
elif cents[0] == '0':   #123,04 ->four cents and not zero four cents
    cents_out = money_units[1][int(cents[1])]
else:
    cents_out = money_units[20][int(cents[0])] + ' ' + money_units[1][int(cents[1])]

dollars_out = 0
s = ''
if len(dollars) == 1:
    dollars_out = money_units[1][int(dollars[0])]
    if money_units[1][int(dollars[0])] == 'one':
        s = ''
    else:
        s = 's'

elif len(dollars) == 2:
    if int(dollars) < 20:
        dollars_out = money_units[10][int(dollars[0 - 1])]
        s = 's'
    else:
        if dollars[1] == '0':
            dollars_out = money_units[20][int(dollars[0])]
        else:
            dollars_out = money_units[20][int(dollars[0])] + ' ' + money_units[1][int(dollars[1])]

        if money_units[1][int(dollars[1])] == 'one':
            s = ''
        else:
            s = 's'

print(f'{dollars_out} dollar{s} {cents_out} cents')

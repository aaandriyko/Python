#Exercise 1: Output floor, flat's number and flat's order in a 9-floor building
i = int(input("Enter  flat number: "))

if i <= 36:
    print("1st Entrance")
    y = 1
elif i <= 72:
    print("2nd Entrance")
    i -= 36
    y = 1
elif i <= 108:
    print("3rd Entrance")
    i -= 72
    y = 1
elif i <= 144:
    print("4th Entrance")
    i -= 108
    y = 1
else:
    y = 0

match y:
    case 0:
        print("No such flat in this building")
    case 1:
        print(f"Floor: {(i - 1) // 4 + 1}")
        number = i % 4

        if not number:
            print("Flat's order: 4")
        else:
            print("Flat's order: ", number)

            
#Or
#FLOORS = 9
#FLATS_ON_FLOOR = 4
#NUMBER_OF_ENTRANCES = 4
#
#flat = int(input('Flat number = '))
#
#if 0 < flat <= FLATS_ON_FLOOR * FLOORS * NUMBER_OF_ENTRANCES:
#    
#    entrance = (flat - 1) // (FLATS_ON_FLOOR * FLOORS) + 1
#    floor = (flat - 1) // FLATS_ON_FLOOR - (entrance - 1) * FLOORS + 1
#    flat_on_floor = (flat - 1) % 4 + 1
#    
#print(flat, entrance, floor, flat_on_floor)
#
#else:
#    print('Wrong flat number')



#----------------------------------------------------------------



#Exercise 2: Leap year
year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("A leap year")
else:
    print("Not a leap year")

    
    
#----------------------------------------------------------------



#Exercise 3: Does a triangle exist?
a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("This triangle exists")
else:
    print("This triangle can't exist")
    
    
#Or
#a, b, c = int(input('a=')), int(input('b=')), int(input('c='))
#Or
#a, b, c = int(input('a=')),\
           int(input('b=')),\
           int(input('c='))

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



#Exercise 2: Leap year
year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("A leap year")
else:
    print("Not a leap year")



#Exercise 3: Does a triangle exist?
a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("This triangle exists")
else:
    print("This triangle can't exist")
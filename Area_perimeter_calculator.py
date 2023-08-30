error = "Please enter a number more than zero"
error_int = "Please enter a number"

again = ""
while again == "":

    loop_1 = False
    while not loop_1:
        try:
            width = float(input("Please input width (must be number): "))
            if width > 0:
                loop_1 = True
            else:
                print()
                print(error)
                print()
        except ValueError:
            print()
            print(error_int)
            print()

    loop_2 = False
    while not loop_2:
        try:
            height = float(input("Please input height (must be number): "))
            if height > 0:
                loop_2 = True
            else:
                print()
                print(error)
                print()
        except ValueError:
            print()
            print(error_int)
            print()

    unit = input("Please enter unit of measurement: ")
    perimeter = (2 * width) + (2 * height)
    area = width * height
    print("the perimeter for the shape is {} {}".format(perimeter, unit))
    print("the area for your shape is {} {}^2".format(area, unit))
    print()

    again = input("press <enter> to rerun, any other key to end: ")

print()
print("Thank you for using the area perimeter calculator")

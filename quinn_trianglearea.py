# Tyler Quinn
# CPSC 21000 - Programming Fundamentals



go_again = 0

while go_again == 0:

   



    base = float(input('Input the base of the triangle: '))
    print('')
    height = float(input('Input the height of the triangle: '))
    print('')
    sideOne = float(input('Input the length of side one: '))
    print('')
    sideTwo = float(input('Input the length of side two: '))
    print('')
    sideThree = float(input('Input the length of side three: '))
    print('')

    #Find the area 

    area = base * height/2

    #print(area)

    print('')

    #print(type(area))

    #print('The area of the triangle is %.2f.' %(area))

    print('')


    #Find the triangle type 

    if sideOne != sideTwo and sideOne != sideThree and sideTwo != sideThree: 
        #find_type = Scalene 
        find_type = 'This scalene triangle has an area of %.2f.' %(area)
        print(find_type)

    elif sideOne == sideTwo and sideOne == sideThree and sideTwo == sideThree: 
        #find_type = Equilateral
        find_type = 'This equilateral triangle has an area of %.2f.' %(area)
        print(find_type)

    else: 
        #find_type = Isosceles 
        find_type = 'This isosceles triangle has an area of %.2f.' %(area)
        print(find_type)


    print('')
    print('Would you like to go again?')
    print('')
    print('')
    print('0: I would like to go again')
    print('1: I am finished')
    print('')
    go_again = float(input('Enter the number which applies: '))

while go_again == 1: 
    print('')
    print('Thank you for using this program.')
    go_again = 2
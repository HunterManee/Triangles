
#Get input from user and store in dictionary (side['a'])
side = {
    'a': int(input()),
    'b': int(input()),
    'c': int(input()),
}

#Quick lookup :P
a = side['a']
b = side['b']
c = side['c']

#All the following condintions must hold for
#the sides to make a triangle:
isTriangle = True
if a + b <= c:
    isTriangle = False
elif a + c <= b:
    isTriangle = False
elif b + c <= a:
    isTriangle = False

#Are the sides able to form a triangle?
if isTriangle == False:
    print(f"{a}, {b}, and {c} do not form a triangle")

#If the sides are able to form a triangle then:
if isTriangle == True:
    #equilateral triangle
    if a == b == c:
        print(f"{a}, {b}, and {c} form an equilateral triangle")
    #isosceles triangle
    elif a == b != c:
        print(f"{a}, {b}, and {c} form an isosceles triangle")
    elif a != b == c:
        print(f"{a}, {b}, and {c} form an isosceles triangle")
    elif a == c != b:
        print(f"{a}, {b}, and {c} form an isosceles triangle")
    #scalene triangle
    elif a != b != c:
        print(f"{a}, {b}, and {c} form a scalene triangle")

    #Exchange display variable
    side1 = a
    side2 = b
    side3 = c

    #Set 'C' to the largest number
    C = max([a, b, c])
    '''
        'a' can equal 'a' as long as it doesn't
        equal the largest number 'C'
        otherwise exhange with expected
        largest number 'c'
    '''
    a = a if a != C else c
    b = b if b != C else c

    #if a * a + b * b == c * c:
    if a ** 2 + b ** 2 == c ** 2:
        print(f"{side1}, {side2}, and {side3} form a Pythagorean triple")
    else:
        print(f"{side1}, {side2}, and {side3} do not form a Pythagorean triple")


  
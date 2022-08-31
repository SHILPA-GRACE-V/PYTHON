def areaOfCircle(radius):
    res=3.14*(radius**2)
    return res

def areaOfRectangle(side1,side2):
    res=side1*side2
    return res

def areaOfSquare(length):
    res=2*length
    return res

def PerimeterOfCircle(radius):
    res=2*3.14*radius
    return res

def PerimeterOfRectangle(side1,side2):
    res=2*(side1+side2)
    return res

def PerimeterOfSquare(length):
    res=4*length
    return res

while True:
    print("1 for Area of  Circle\n"  
           "2 for Area of Rectangle\n"
            "3 for Area of Square\n"
            "4 for Perimeter of Circle\n"
            "5 for Perimeter of Rectangle\n"
            "6 for Perimeter of Square\n"
            "7 for Exit\n"  )

    choice=int(input("Enter your choice : "))

    if(choice==1):
        radius=int(input("Enter the radius:"))
        result=areaOfCircle(radius)
        print(result)

    if(choice==2):
        side1=int(input("Enter the length:"))
        side2=int(input("Enter the width:"))
        result=areaOfRectangle(side1,side2)
        print(result)

    if(choice==3):
        length=int(input("Enter the length:"))
        result=areaOfSquare(length)
        print(result)

    if(choice==4):
        radius=int(input("Enter the radius:"))
        result=PerimeterOfCircle(radius)
        print(result)

    if(choice==5):
        side1=int(input("Enter the length:"))
        side1=int(input("Enter the width:"))
        result=PerimeterOfRectangle(side1,side2)
        print(result)

    if(choice==6):
        length=int(input("Enter the length:"))
        result=PerimeterOfSquare(length)
        print(result)

    else:
        break

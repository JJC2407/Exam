print(" Menu\n------\n 1.Triangle\n 2.Rectangle\n 3.Circle\n 4.Exit")
a=int(input("Enter your option : "))
while(a!=4):
    if(a==1):
        print(" Triangle \n----------")
        h=int(input("Enter the hieght of triangle : "))
        b=int(input("Enter the base of triangle : "))
        print("\nArea of Triangle is : ",.5*h*b)
    if (a == 2):
        print("\n Rectangle \n-----------")
        l=int(input("Enter the length of rectangle : "))
        w=int(input("Enter the width of triangle : "))
        print("\nArea of Rectangle is : ",l*w)
    if (a == 3):
        print(" Circle \n--------")
        r=int(input("Enter the radius of circle : "))
        print("\nArea of Circle is : ",3.14*r*r)
    print(" Menu\n------\n 1.Triangle\n 2.Rectangle\n 3.Circle\n 4.Exit")
    a = int(input("Enter your option : "))


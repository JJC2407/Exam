def compare():
    b=0
    n=int(input("Enter the length of first list : "))
    n2=int(input("Enter the length of second list : "))
    list1=[]
    print("Enter the strings in first list : \n")
    for i in range(n):
        list1.append(input())
    list2=[]
    print("Enter the strings in second list : \n")
    for i in range(n2):
        list2.append(input())
    a=int(input("Enter the no.of strings to be compare : "))
    for i in range(a):
        if(list1[i]==list2[i]):
            b=b+1
    if(a==b):
        print("true")
    else:
        print("false")
compare()
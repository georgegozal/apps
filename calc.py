nums = input("შეიყვანეთ მაგალითი \n მაგ, 2+4 >> ").replace(" ", "")
x= ['+', '-', '*', "**", 'x', '/', ':', '%']


def calc(n, m):
    
    mylist = []
    for s in x :
        if s in n:
            mylist = n.split(s)
            break
                       
    return mylist, s

#ფუქნციის გამოძახება შედეგის სანახავად 
mynums, y  = calc(nums, x)

#გამოსათვლელი ფუნქცია 
def gamotvla(l, y):
    
    if y == "-":
        return int(l[0]) - int(l[1]) 
    elif y == "+":
        return int(l[0]) + int(l[1])
    elif y == "*" or y =="x":
        return int(l[0]) * int(l[1])
    elif y == "/" or y == ":":
        return int(l[0]) / int(l[1])
       
#ფუქნციის გამოძახება შედეგის სანახავად 
print(gamotvla(mynums, y))  

##for i in range(5):
##    for j in range(5):
##        print('*')
##    print('\n')
##A
for i in range(5):
    if i==0 or i==2:
        print("*"*5)

    else:
        print("*"+" "*3+"*")
##B
for i in range(5):
    if i==0 or i==2 or i==4:
        print("*"*5)

    else:
        print("*"+" "*3+"*")

##C
for i in range(5):
    if i==0 or i==4 :
        print("*"*5)

    else:
        print("*"+" "*3)
##D
for i in range(5):
    if i==0 or i==4 :
        print("*"*5)

    else:
        print("*"+" "*4+"*")
##E
for i in range(5):
    if i==0 or i==4 or i==2 :
        print("*"*5)

    else:
        print("*"+" "*2)

##F
for i in range(5):
    if i==0 or i==4 :
        print("*"*5)
    elif i==3:
            print("*"+""*3+"*")
    elif i==2:
            print("*"+""*2+"*"*2)

    else:
        print("*"+" "*2)

##G
for i in range(5):
    if i==0 or i==2 :
        print("*"*5)

    else:
        print("*"+" "*2)
##H
        

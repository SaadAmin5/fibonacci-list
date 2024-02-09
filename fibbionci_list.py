# fibbionci list

# creating its function

def factorial (number):
    
    a=0
    b=1
    sum1=0
    aa=[0,1]

    for i in range(1, number-1):

 
        sum1=a+b

        aa.append(sum1)  

        a=b
        b=sum1

    print(aa)

num=int(input('enter factorial number: '))
factorial(number=num)
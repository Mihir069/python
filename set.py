def fact(num):
    if num ==1 or num ==0:
        return 1 
    return num*fact(num-1)

    
x = int(input("Enter x : "))
n = int(input("Enter n : "))

finalResult = 1
arith = '-'
for i in range(2,n+1,2):
    result = (x**i)/fact(i)
    
    if arith == '-':
        finalResult = finalResult-result
        arith = '+'

    elif arith == '+':
        finalResult = finalResult+result
        arith = '-'




print(finalResult)

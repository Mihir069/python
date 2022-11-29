n = int(input("Enter the number of terms:"))
x = int(input("Enter the value of x:"))
sum1 = 1
def fac_func():
    fact = 1
    s = -1
    for i in range(2,2*n):
        fact = fact*i*(i-1)
        s= s*(1)
        sum1 =(s*(pow(x,i))/fact)
        result = 1-sum1
    print(result)
fac_func()



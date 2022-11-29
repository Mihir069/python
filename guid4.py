#ad-1259
number = int(input("Enter the number :"))
def function_of_num(number):
    num_set = set()
    while(number!=0):
        dig=number%10
        number = number//10
        num_set.add(dig)
        print(num_set)
function_of_num(number)

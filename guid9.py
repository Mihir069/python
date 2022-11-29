#WAP to input n no of marks and rollno of student and print the higest marks.
def higher_mark():
    D={}
    n=int(input('Enter no. of students'))
    for i in range(n):
        name=(input('enter name od student :'))
        m=int(input('enter marks :'))
        D[name]=m
    max=0
    for i in D:
        if D[i]>max:
            max=D[i]
            p=i
    print('roll no :',p) 
    print('Higest marks :',max)
higher_mark()

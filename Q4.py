#quetion 4
row = int(input("Enter the number of row :"))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
for i in range(row ,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("")
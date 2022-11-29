t1 = (1,2,5,7,9,2,4,6,8,10)
while True:
    print("\nMenu")
    print("1) Print another tuple whose values are even numbers in the given tuple.")
    print("2) Concatenate a tuple t2 = (11,13,15) with t1.")
    print("3) Return maximum and minimum value from this tuple.")
    ch1 = int(input("Enter your choice :"))
    print("\n")
    
    if ch1 == 1:
        print("\nMenu")
        print("1) Print another tuple whose values are even numbers in the given tuple.")
        print("2) Concatenate a tuple t2 = (11,13,15) with t1.")
        print("3) Return maximum and minimum value from this tuple.")
        ch2 = int(input("Enter your choice :"))
        print("\n")

        if ch2 == 1:
            for i in range(len(t1)):
                if t1[i]%2==0:
                    print(t1[i],end=" ")
        elif ch2 == 2:
            t2 = (11,13,15)
            new_t1 = t1+t2
            print("Concatination between t1 and t2 is : ")
            print(new_t1,end=" ")
        elif ch2 == 3:
            print("maximum value of t1 :",max(t1))
            print("minimum value of t1 :",min(t1))
            break
        else:
            print("Wrong Input...")
    else:
        print("Wrong Input...")
                

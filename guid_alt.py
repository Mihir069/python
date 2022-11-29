def areAllNum(lis):
    for i in lis:
        if isinstance(i, int):
            pass
        else:
            return False
    else :
        return True


def areAllString(lis):
    for i in lis : 
        if isinstance(i, str):
            pass
        else:
            return False
    else:
        return True   



def numberOfOddElements (lis):
    count = 0
    for i in lis:
        if i % 2 != 0:
            count +=1
        pass

    return count

def reverseList (lis):
    return lis[::-1]

def search (lis,element):
    if element in lis:
        return lis.index(element)
    else :
        return False

def sortInDesending(lis):
    lis.sort()
    return reverseList(lis)

def commom_members (lis1,lis2):
    commom = []
    for i in lis1 : 
        if i in lis2:
            commom.append(i)
        pass
    return commom 

def largestString (lis):
    temp = lis[0]
    for i in lis:
        if len(i) > len(temp):
            temp = i 
    return temp


def main():
    list1  = [45,34,24,54,343]
    list2  = ["Chandan","Ayush","Mihir","Fan"]

    print("Current list is ",list1)
    print(f"Are all elements in list are numbers ? ")
    print(areAllNum(list1))
    print()

    print (f"number of odd element in list ")
    print(numberOfOddElements(list1))
    print()

    print("list in reverse") 
    print(reverseList(list1))
    print()

    print("is 69 present in list")
    print(search(list1,69))
    print()
    
    print("removing 54 from list")
    list1.remove(54)

    print()
    print("list in Desending order")
    print(sortInDesending(list1))

    print("---------------------------------------------------------")
    print("Current list is ",list2)
    print(f"\nAre all elements in list is string ")
    print(areAllString(list2))
    print()

    print(f"Largest string in the list")
    print(largestString(list2))
    print()

    print("list in reverse form")
    print(reverseList(list2))
    print()

    print("Searcing \"Ayush\" in list ")
    print(search(list2,"Ayush"))
    print()
    print("Removing \"Fan\" from list")
    list2.remove("Fan")
    print()

    print("List in deseding order")
    print(sortInDesending(list2))
    

    print("\nCommon memebers in both list")
    commom_members(list1,list2)

if _name_ == "_main_":
    main()

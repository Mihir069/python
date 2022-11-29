lst1 = ['1','2','35','23','12']
lst2 = ['a','d','f','e','t']
lst3 = [3,'v',9,34,'l','p']

def check_for_element():
    result = all(ele.isdigit() for ele in lst1)
    if (result == True):
        print("All the elemnts in the lists are numeric")
    else:
        print("All the elemnts in the lists are not numeric ")
check_for_element()

def check_for_numaric():
    even_count =0
    odd_count = 0
    result = all(ele.isdigit() for ele in lst1)
    if(result == True):
        for ele in lst1:
            if int(ele)%2 == 0:
                even_count +=1
                print("number of even :",even_count)
            else:
                odd_count +=1
                print("number of odd",odd_count)
    else:
        print("..")
check_for_numaric()

def reverse_list():
    lst1.reverse()
    print(lst1)
reverse_list()
def sort_list():
    lst1.sort()
    print(lst1)
sort_list()
            

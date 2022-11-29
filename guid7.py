srt1 = input("Enter any String :")
srt2 = input("Enter any String :")
srt3 = input("Enter any String :")

def len_of_srt():
    len_srt1 = len(srt1)
    len_srt2 = len(srt2)
    len_srt3 = len(srt3)
    print("length of given string three is:",len_srt1," ",len_srt2," ",len_srt3)
def max_of_srt():
    max_srt1 = max(srt1)
    max_srt2 = max(srt2)
    max_srt3 = max(srt3)
    print("The max of three strings is :",max_srt1," ",max_srt2," ",max_srt3)
def num_in_srt():
    num_srt1 = len(srt1.split(',',3))
    num_srt2 = len(srt2.split())
    num_srt3 = len(srt3.split())
    print("Number of words in string :",str(num_srt1)," ",str(num_srt1)," ",str(num_srt1))
def replace_of_srt(test_str,K):
    vowels = 'AEIOUaeiou'
    for ele in  vowels:
        test_str = test_str.replace(ele,K)
    return test_str
def palindrome_of_srt():
    reverse_srt1 = reversed(srt1)
    if list(srt1) == list(reverse_srt1):
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
while True:
    print("MENU...")
    print("1. Find the length of string")
    print("2. Return maximum of three strings")
    print("3. Accept a string and replace all vowels with'#'")
    print("4. Find number of words in the given string")
    print("5. Check whether the string is a palindrome or not")
    ch = int(input("Enter your choice :"))
    if ch == 1:
        print("MENU...")
        print("1. Find the length of string")
        print("2. Return maximum of three strings")
        print("3. Accept a string and replace all vowels with'#'")
        print("4. Find number of words in the given string")
        print("5. Check whether the string is a palindrome or not")
        ch = int(input("Enter your choice :"))
        if ch == 1:
            len_of_srt()
        elif ch == 2:
            max_of_srt()
        elif ch == 3:
            num_in_srt()
        elif ch == 4:
            input_str = "This is string "
            K = "#"
            print(replace_of_srt(input_str,K))
        elif ch == 5:
            palindrome_of_srt()
            break
        else:
            print("Exit")
    else:
        print("Try only 1....")
            
            

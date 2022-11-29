def marks(stu, sct):
    for i in range(stu):
        name = input("\nEnter the name of Student {}: ".format(i + 1))
        marks = []
        for j in range(4):
            subject = float(input("Enter the marks of Subject {}: ".format(j + 1)))
            marks.append(subject)
        sct[name] = marks
        print("\n{0}'s marks are {1} ".format(name, sct[name]))

def percentage(sct):
    top = 'null'
    per = 0.0
    for key, value in sct.items():
        curr_per = sum(value)/4
        if curr_per > per:
            per = curr_per
            top = key
    return top, per

sct = {}
stu = int(input("Enter the total number of students :- "))
marks(stu, sct)
print(sct)
print("\nThe student with highest percentage is ", percentage(sct))

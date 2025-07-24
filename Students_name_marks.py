def Student_Marks(Students):
    print("{:<25} {:<5}".format("Students_name","Students_mark"))
    print("_"*40)
    for name,score in Students:
        print("{:<25} {:<5}".format(name,score))
Students_list = [
    ("Urvashi",88),
    ("Aman",95),
    ("Suraj",99),
    ("Priya",98),
]
Student_Marks(Students_list)

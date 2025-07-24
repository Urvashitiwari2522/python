def display_student_scores(student_list):
  print("{:<20} {:>6}".format("Student Name", "Score"))
  print("-" * 30)
  for name, score in student_list:
    print("{:<20} {:>6}".format(name, score))
 # Sample Input
students = [
    ("Urvashi", 95),
    ("Anjali", 89),
    ("Rohit", 78),
    ("Simran", 88)
 ]
 # Call the function
display_student_scores(students)
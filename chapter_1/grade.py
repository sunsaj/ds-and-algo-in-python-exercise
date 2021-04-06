print("Welcome to CGPA Calculator")
print("Please enter your grades one line at a time")
print("Enter a blank line to end your input")

points = {'A+':5, 'A':4.5, 'B+': 4, 'B':3.5, 'C+':3, 'C':2.5, 'D+':2, 'D':2, 'F':0}

no_of_courses = 0
total_point = 0

done = False

while not done:
    grade = input()
    
    if grade == '':
        done=True
    elif grade not in points:
        print("You have entered unknown grade, continue..")
    else:
        no_of_courses += 1
        total_point += points[grade]

if no_of_courses > 0:
    print(f"Your CGPA is {total_point/no_of_courses:.3}")

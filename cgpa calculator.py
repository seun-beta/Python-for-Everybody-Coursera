number_of_courses = 0
print ('Welcome to this cgpa calculator')
print ('''Type 'done' to end this calculator''')
previous_CGPA  =  float (input('Input your previous CGPA else input zero'))
previous_unit  =  float (input('Input your previous units else input zero'))
while True :
    grade = (input('Please input your score for the course: '))
    unit= (input('Please input the units of this course '))
    if grade == 'done' or unit == 'done' :
        break
    try :
        grade = int(grade)
        unit= int(unit)
    except :
        print ('You have to input a number')
        continue
    if grade > 100 :
        print('''Your grade can't be greater than 100''')
        continue
    elif grade >= 70 :
        points = 7
    elif grade >= 65 :
        points = 6
    elif grade >= 60 :
        points = 5
    elif grade >= 55 :
        points = 4
    elif grade >= 50 :
        points = 3
    elif grade >= 45 :
        points = 2
    elif grade >= 40 :
        points = 1
    else :
        points = 0
    number_of_courses = number_of_courses + 1
    GPA = (previous_CGPA * previous_unit)+((points*unit)/ number_of_courses)
print ('Your CGPA is',GPA)

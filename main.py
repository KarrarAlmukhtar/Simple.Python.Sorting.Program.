numGrades = int(input('How many grades do you have: '))
grades = []
bucket = 0
lowGrade = 100
highGrade = 0
for i in range(0, numGrades, 1):
    grade = float(input('Please input your grades: '))
    grades.append(grade)
    print(grades)
print('Yor grades are: ')
for i in range(0, numGrades, 1):
    print(grades[i])
for i in range(0, numGrades, 1):
    bucket = bucket + grades[i]
average = bucket / numGrades
print('')
print('Your average is: ', average)
for i in range(0, numGrades, 1):
    if grades[i] < lowGrade:
        lowGrade = grades[i]
        print('Your low grade is: ', lowGrade)
for i in range(0, numGrades, 1):
    if grades[i] > highGrade:
        highGrade = grades[i]
        print('Your high grade is: ', highGrade)
for i in range(0, numGrades-1, 1):
    for i in range(0, numGrades-1, 1):
        if grades[i] < grades[i+1]:
            swp = grades[i] = grades[i+1]
            grades[i+1] = swp
print('Your sorted grades list is: ')
for i in range(0, numGrades, 1):
    print(grades[i])

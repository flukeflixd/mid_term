print('''========================================
| Program Caculate Grade Point Average |
========================================''')
All = 5 * 3
Sum = 0
List = []
grades = []
scores = []
points = []
no = 0
print("Input Data:")
for n in range(1,5+1):
    List.append(input(f"Enter subject name({n}) : "))
    score = int(input(f"Enter subject score({n}) : "))
    scores.append(score)
    print()
    if score >= 80 and score <= 100:
        grade = 'A'
        credit = 4.0
        point = credit * 3.0
    elif score >= 70 and score <= 79:
        grade = 'B'
        credit = 3.0
        point = credit * 3.0
    elif score >= 60 and score <= 69:
        grade = 'C'
        credit = 2.0
        point = credit * 3.0
    elif score >= 50 and score <= 59:
        grade = 'D'
        credit = 1.0
        point = credit * 3.0
    elif score >= 0 and score <= 49:
        grade = 'F'
        credit = 0.0
        point = credit * 3.0
    Sum += point
    grades.append(grade)
    points.append(point)
print(f'''\t Grade Point Average(GPA) Report
=================================================
No. Subject Name\t Mark  Grade    Points
=================================================''')

for n in range(0,5):
    no += 1
    print(f"{no:<4} {List[n]:<22}{scores[n]:<6} {grades[n]:<6} {points[n]:<5.1f}")

print("=================================================")
gpa = Sum / All 
print(f"Total Points :%.1f "%Sum)
print(f"Total Credit :%.1f "%All)
print(f"Grade Point Average(GPA) :%.2f "%gpa)
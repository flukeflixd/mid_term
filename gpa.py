print("Input Data")

subject_name_list = []
score_list =[]
gpa_list = []
point_list = []
credit_list = []

number = 0

for i in range(1,5+1):
    subject_name = input(f"Enter Subject Name ({i}) : ")
    subject_name_list.append(subject_name)
    score = int(input(f"Enter subject score ({i}) : "))
    score_list.append(score)
    print()


print(subject_name_list)
print(score_list)

for score in score_list:
    if score >= 80 and score <= 100: 
        gpa_list.append("A")
        credit = 4.0
        point = credit * 3.0
    elif score >= 70 and score <= 79:
        gpa_list.append("B")
        credit = 3.0
        point = credit * 3.0
    elif score >= 60 and score <= 69:
        gradeC = 'C'
        gpa_list.append("C")
        credit = 2.0
        point = credit * 3.0
    elif score >= 50 and score <= 59:
        gpa_list.append("D")
        credit = 1.0
        point = credit * 3.0
    elif score >= 0 and score <= 49:
        gpa_list.append("F")
        credit = 0
        point = credit * 3.0
    point_list.append(point)
    credit_list.append(credit)

print(gpa_list)
print(point_list)
print("\tGrade Point Average(GPA) Report")
print("="*40)
print("No. Subject Name\tMark Grade\tPoints")
print("="*40)

for i in range(1,5+1):
    number += 1
   # print(f"{number} {subject_name_list[i]}\t{score_list[i]}\n{gpa_list[i]}\n{point_list[i]}")

print("="*40)
print(f"Total Points : {sum(point_list)}")
print(f"Total Credit : {sum(credit_list)}")
print(f"Grade Point Average(GPA) : {sum(point_list) / sum(credit_list):.2f}")
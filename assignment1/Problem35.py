#Use elif to grade students based on score.
def grade_student(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Example Usasge
print(grade_student(95))  # A
print(grade_student(82))  # B
print(grade_student(74))  # C
print(grade_student(61))  # D
print(grade_student(45))  # F

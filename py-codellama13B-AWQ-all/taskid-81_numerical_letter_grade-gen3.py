from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    >>> grade_equation([4.0, 3, 1.7, 2, 3.5])
    ['A+', 'B', 'C-', 'C', 'A-']
    """

    grade_list = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    gpa_grade = []
    for gpa in grades:
        if gpa == 4.0:
            gpa_grade.append(grade_list[0])
        elif gpa > 3.7:
            gpa_grade.append(grade_list[1])
        elif gpa > 3.3:
            gpa_grade.append(grade_list[2])
        elif gpa > 3.0:
            gpa_grade.append(grade_list[3])
        elif gpa > 2.7:
            gpa_grade.append(grade_list[4])
        elif gpa > 2.3:
            gpa_grade.append(grade_list[5])
        elif gpa > 2.0:
            gpa_grade.append(grade_list[6])
        elif gpa > 1.7:
            gpa_grade.append(grade_list[7])
        elif gpa > 1.3:
            gpa_grade.append(grade_list[8])
        elif gpa > 1.0:
            gpa_grade.append(grade_list[9])
        elif gpa > 0.7:
            gpa_grade.append(grade_list[10])
        elif gpa > 0.0:
            gpa_grade.append(grade_list[11])
        else:
            gpa_grade.append(grade_list[12])
    return gpa_grade

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

    A_Plus = [4.0, 4.0]
    A = [3.7, 3.7]
    A_ = [3.3, 3.3]
    B_Plus = [3.0, 3.0]
    B = [2.7, 2.7]
    B_ = [2.3, 2.3]
    C_Plus = [2.0, 2.0]
    C = [1.7, 1.7]
    C_ = [1.3, 1.3]
    D_Plus = [1.0, 1.0]
    D = [0.7, 0.7]
    D_ = [0.0, 0.0]
    E = [0.0, 0.0]

    letter_grades = []

    for i in grades:
        if i in A_Plus:
            letter_grades.append('A+')
        elif i in A:
            letter_grades.append('A')
        elif i in A_:
            letter_grades.append('A-')
        elif i in B_Plus:
            letter_grades.append('B+')
        elif i in B:
            letter_grades.append('B')
        elif i in B_:
            letter_grades.append('B-')
        elif i in C_Plus:
            letter_grades.append('C+')
        elif i in C:
            letter_grades.append('C')
        elif i in C_:
            letter_grades.append('C-')
        elif i in D_Plus:
            letter_grades.append('D+')
        elif i in D:
            letter_grades.append('D')
        elif i in D_:
            letter_grades.append('D-')
        elif i in E:
            letter_grades.append('E')
        else:
            letter_grades.append("Invalid")
    return letter_grades

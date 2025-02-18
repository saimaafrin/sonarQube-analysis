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

    # Your code here
    grades_letter = []
    for gpa in grades:
        if gpa > 4:
            grades_letter.append("A+")
        elif gpa > 3.7 and gpa <= 4:
            grades_letter.append("A")
        elif gpa > 3.3 and gpa <= 3.7:
            grades_letter.append("A-")
        elif gpa > 3 and gpa <= 3.3:
            grades_letter.append("B+")
        elif gpa > 2.7 and gpa <= 3:
            grades_letter.append("B")
        elif gpa > 2.3 and gpa <= 2.7:
            grades_letter.append("B-")
        elif gpa > 2 and gpa <= 2.3:
            grades_letter.append("C+")
        elif gpa > 1.7 and gpa <= 2:
            grades_letter.append("C")
        elif gpa > 1.3 and gpa <= 1.7:
            grades_letter.append("C-")
        elif gpa > 1 and gpa <= 1.3:
            grades_letter.append("D+")
        elif gpa > 0.7 and gpa <= 1:
            grades_letter.append("D")
        elif gpa > 0 and gpa <= 0.7:
            grades_letter.append("D-")
        elif gpa <= 0:
            grades_letter.append("E")
    return grades_letter

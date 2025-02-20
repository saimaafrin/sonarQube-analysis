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

    
    if len(grades) == 0:
        return []
    elif len(grades) == 1:
        if grades[0] > 3.7:
            return ['A']
        elif grades[0] > 3.3:
            return ['A-']
        elif grades[0] > 3.0:
            return ['B+']
        elif grades[0] > 2.7:
            return ['B']
        elif grades[0] > 2.3:
            return ['B-']
        elif grades[0] > 2.0:
            return ['C+']
        elif grades[0] > 1.7:
            return ['C']
        elif grades[0] > 1.3:
            return ['C-']
        elif grades[0] > 1.0:
            return ['D+']
        elif grades[0] > 0.7:
            return ['D']
        elif grades[0] > 0.0:
            return ['D-']
        else:
            return ['E']
    else:
        if grades[0] > 3.7:
            return ['A'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 3.3:
            return ['A-'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 3.0:
            return ['B+'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 2.7:
            return ['B'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 2.3:
            return ['B-'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 2.0:
            return ['C+'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 1.7:
            return ['C'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 1.3:
            return ['C-'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 1.0:
            return ['D+'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 0.7:
            return ['D'] + numerical_letter_grade(grades[1:])
        elif grades[0] > 0.0:
            return ['D-'] + numerical_letter_grade(grades[1:])
        else:
            return ['E'] + numerical_letter_grade(grades[1:])

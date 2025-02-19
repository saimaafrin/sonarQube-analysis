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

    
    def grade_equation(grades: List[float]) -> List[str]:
        """
        Write your code here.
        """
        g = []
        for i in grades:
            if i >= 4.0:
                g.append('A+')
            elif i >= 3.7 and i < 4.0:
                g.append('A')
            elif i >= 3.3 and i < 3.7:
                g.append('A-')
            elif i >= 3.0 and i < 3.3:
                g.append('B+')
            elif i >= 2.7 and i < 3.0:
                g.append('B')
            elif i >= 2.3 and i < 2.7:
                g.append('B-')
            elif i >= 2.0 and i < 2.3:
                g.append('C+')
            elif i >= 1.7 and i < 2.0:
                g.append('C')
            elif i >= 1.3 and i < 1.7:
                g.append('C-')
            elif i >= 1.0 and i < 1.3:
                g.append('D+')
            elif i >= 0.7 and i < 1.0:
                g.append('D')
            elif i >= 0.0 and i < 0.7:
                g.append('D-')
            else:
                g.append('E')
        return g

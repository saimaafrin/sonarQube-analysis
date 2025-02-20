import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // It is the last week of the semester and the teacher has to give the grades
    // to students. The teacher has been making her own algorithm for grading.
    // The only problem is, she has lost the code she used for grading.
    // She has given you an array array list of GPAs for some students and you have to write 
    // a function that can output an array array list of letter grades using the following table:
    // GPA       |    Letter grade
    // 4.0                A+
    // > 3.7                A 
    // > 3.3                A- 
    // > 3.0                B+
    // > 2.7                B 
    // > 2.3                B-
    // > 2.0                C+
    // > 1.7                C
    // > 1.3                C-
    // > 1.0                D+ 
    // > 0.7                D 
    // > 0.0                D-
    // 0.0                E
    // Example:
    // >>> gradeEquation((new ArrayList<Float>(Arrays.asList((float)4.0f, (float)3l, (float)1.7f, (float)2l, (float)3.5f))))
    // (new ArrayList<String>(Arrays.asList((String)"A+", (String)"B", (String)"C-", (String)"C", (String)"A-")))
    public static ArrayList<String> numericalLetterGrade(ArrayList<Float> grades) {

        // TODO: Write a program that returns an array array list of letter grades.
        // [0, 1, 2, 3, 4]  -> [A+, A, B+, C-, C]
        // [10, 20, 30, 40, 50]  -> [A+, A, B+, C-, C]
        // [3.0f, 3.3f, 3.7f, 4.0f] -> [A, A, A, A]
        // [3.3f, 3.7f, 4.0f, 4.3f] -> [A, A, A, B]
        // [1.5f, 2.5f, 3.5f, 4.5f] -> [C-, C, B-, B]
        // [2.3f, 3.3f, 4.3f, 5.3f] -> [C-, C, B-, B]
        // [2.5f, 3.5f, 4.5f, 5.5f] -> [C, C, B, B]
        // [2.6f, 3.6f, 4.6f, 5.6f] -> [C, C, B, B]
        // [2.5f, 3.5f, 4.5f, 5.5f, 6.5f] -> [C, C, B, B, A]
        // [2.5f, 3.5f, 4.5f, 5.5f, 6.5f, 7.5f] -> [C, C, B, B, A, A]
        ArrayList<String> gradeList = new ArrayList<String>();
        for (float grade: grades) {
            if (grade >= 4.0) {
                gradeList.add("A+");
            } else if (grade >= 3.7) {
                gradeList.add("A");
            } else if (grade >= 3.3) {
                gradeList.add("A-");
            } else if (grade >= 3.0) {
                gradeList.add("B+");
            } else if (grade >= 2.7) {
                gradeList.add("B");
            } else if (grade >= 2.3) {
                gradeList.add("B-");
            } else if (grade >= 2.0) {
                gradeList.
    }
    public static void main(String[] args) {
    assert(numericalLetterGrade((new ArrayList<Float>(Arrays.asList((float)4.0f, (float)3l, (float)1.7f, (float)2l, (float)3.5f)))).equals((new ArrayList<String>(Arrays.asList((String)"A+", (String)"B", (String)"C-", (String)"C", (String)"A-")))));
    assert(numericalLetterGrade((new ArrayList<Float>(Arrays.asList((float)1.2f)))).equals((new ArrayList<String>(Arrays.asList((String)"D+")))));
    assert(numericalLetterGrade((new ArrayList<Float>(Arrays.asList((float)0.5f)))).equals((new ArrayList<String>(Arrays.asList((String)"D-")))));
    assert(numericalLetterGrade((new ArrayList<Float>(Arrays.asList((float)0.0f)))).equals((new ArrayList<String>(Arrays.asList((String)"E")))));
    assert(numericalLetterGrade((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)0.3f, (float)1.5f, (float)2.8f, (float)3.3f)))).equals((new ArrayList<String>(Arrays.asList((String)"D", (String)"D-", (String)"C-", (String)"B", (String)"B+")))));
    assert(numericalLetterGrade((new ArrayList<Float>(Arrays.asList((float)0.0f, (float)0.7f)))).equals((new ArrayList<String>(Arrays.asList((String)"E", (String)"D-")))));
    }

}

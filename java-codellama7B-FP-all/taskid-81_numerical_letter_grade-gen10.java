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

        ArrayList<String> output = new ArrayList<String>();
        for (int i = 0; i < grades.size(); i++) {
            switch (grades.get(i)) {
            case 4.0f:
            case 3.7f:
            case 3.3f:
            case 3.0f:
            case 2.7f:
            case 2.3f:
            case 2.0f:
            case 1.7f:
            case 1.3f:
            case 1.0f:
            case 0.7f:
            case 0.3f:
            case 0.0f:
                output.add("D-");
                break;
            case 3.4f:
            case 3.1f:
            case 2.4f:
            case 2.1f:
            case 1.4f:
            case 1.1f:
            case 0.4f:
            case 0.0f:
                output.add("E");
                break;
            case 3.5f:
            case 3.2f:
            case 2.5f:
            case 2.2f:
            case 1.5f:
            case 1.2f:
            case 0.5f:
                output.add("D+");
                break;
            case 3.6f:
            case 3.3f:
            case 2.6f:
            case 2.3f:
            case 1.6f:
            case 1.3f:
            case 0.6f:
                output.add("D");
                break;
            case 3.8f:
            case 3.5f:
            case 2.8f:
            case 2.5f:
            case 1.8f:
            case 1.5f:
            case 0.8f:
            case 0.5f:
                output.add("D-");
                break;
            case 3.9f:
            case 3.6f:
            case 2.9f:
            case 2.6f:
            case 1.9f:
            case 1.6f:
            case 0.9f:
            case 0.6f:
                output.add("D");
                break;
            case 4.0f:
            case 3.
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

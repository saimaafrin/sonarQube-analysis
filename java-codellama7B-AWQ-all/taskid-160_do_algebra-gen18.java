import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given two array lists operator, and operand. The first array list has basic algebra operations, and 
    // the second array list is an array array list of integers. Use the two given array lists to build the algebric 
    // expression and return the evaluation of this expression.
    // The basic algebra operations:
    // Addition ( + ) 
    // Subtraction ( - ) 
    // Multiplication ( * ) 
    // Floor division ( // ) 
    // Exponentiation ( ** ) 
    // Example:
    // operator['+', '*', '-']
    // array array list = [2, 3, 4, 5]
    // result = 2 + 3 * 4 - 5
    // => result = 9
    // Note:
    // The length of operator array list is equal to the length of operand array list minus one.
    // Operand is an array array list of of non-negative integers.
    // Operator array list has at least one operator, and operand array list has at least two operands.
    public static long doAlgebra(ArrayList<String> op, ArrayList<Long> operand) {

        // Calculate length of operand and operator
        int length = operand.size();
        // Create two variables to store the final result of the calculation
        long result = 0;
        // Create variable for the second operand and the operation to be done on it
        long second = 0;
        String operation = "";
        // Create two variables to store the first and second operands
        long first = 0;
        long second1 = 0;
        // Create a variable to store the operation to be done
        String operation1 = "";
        // Create a variable to store the result of the operation
        long result1 = 0;
        // Create a variable to store the result of the operation
        long result2 = 0;
        // Create a variable to store the result of the operation
        long result3 = 0;
        // Create a variable to store the result of the operation
        long result4 = 0;
        // Create a variable to store the result of the operation
        long result5 = 0;
        // Create a variable to store the result of the operation
        long result6 = 0;
        // Create a variable to store the result of the operation
        long result7 = 0;
        // Create a variable to store the result of the operation
        long result8 = 0;
        // Create a variable to store the result of the operation
        long result9 = 0;
        // Create a variable to store the result of the operation
        long result10 = 0;
        // Create a variable to store the result of the operation
        long result11 = 0;
        // Create a variable to store the result of the operation
        long result12 = 0;
        // Create a variable to store the result of the operation
        long result13 = 0;
        // Create a variable to store the result of the operation
        long result14 = 0;
        // Create a variable to store the result of the operation
        long result15 = 0;
        // Create a variable to store the result of the operation
        long result16 = 0;
        // Create a variable to store the result of the operation
        long result17 = 0;
        // Create a variable to store the result of the operation
        long result18 = 0;
        // Create a variable to store the result of the operation
        long result19 = 0;
        // Create a variable to store the result of the operation
        long result20 = 0;
        // Create a variable to store the result of the operation
        long result21 = 0;
        // Create a variable to store the result of the operation
        long result22 = 0;
        // Create a variable to store the result of the operation
        long result23 = 0;
        // Create a variable to store the result of the operation
        long result24 = 0;
        // Create a variable to store the result of the operation
        long result25 = 0;
        // Create a variable
    }
    public static void main(String[] args) {
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"**", (String)"*", (String)"+"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (37l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"+", (String)"*", (String)"-"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (9l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"//", (String)"*"))), (new ArrayList<Long>(Arrays.asList((long)7l, (long)3l, (long)4l)))) == (8l));
    }

}

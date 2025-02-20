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

        // Write your code here
        int len = op.size();
        String[] op_arr = new String[len];
        long[] operand_arr = new long[len];

        for (int i = 0; i < len; i++) {
            op_arr[i] = op.get(i);
            operand_arr[i] = operand.get(i);
        }
        int index = 0;
        String op1 = "", op2 = "";
        long first, second;
        String sign = "";
        for (int i = 0; i < len; i++) {
            if (i != 0) {
                sign = op_arr[i];
                if (sign.equals("*"))
                    first *= operand_arr[index];
                else if (sign.equals("+"))
                    first += operand_arr[index];
                else if (sign.equals("-"))
                    first -= operand_arr[index];
                else
                    first /= operand_arr[index];
                index++;
            } else {
                first = operand_arr[i];
            }
        }
        return first;
    }
    public static void main(String[] args) {
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"**", (String)"*", (String)"+"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (37l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"+", (String)"*", (String)"-"))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)4l, (long)5l)))) == (9l));
    assert(doAlgebra((new ArrayList<String>(Arrays.asList((String)"//", (String)"*"))), (new ArrayList<Long>(Arrays.asList((long)7l, (long)3l, (long)4l)))) == (8l));
    }

}

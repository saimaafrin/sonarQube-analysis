import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, return the count of the numbers of n-digit
    // positive integers that start or end with 1.
    public static long startsOneEnds(long n) {

        // Initialize the solution with 0.
        long solution = 0;

        // Iterate over all the possible n-digit numbers.
        for (long i = 1; i <= (long) Math.pow(10, n); i++) {
            // Get the number as a string.
            String number = Long.toString(i);

            // Check if the number starts or ends with 1.
            if (number.startsWith("1") || number.endsWith("1")) {
                // Increment the solution.
                solution++;
            }
        }

        // Return the solution.
        return solution;
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}

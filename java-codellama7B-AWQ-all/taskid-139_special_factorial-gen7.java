import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // The Brazilian factorial is defined as:
    // brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    // where n > 0
    // For example:
    // >>> specialFactorial((4l))
    // (288l)
    // The function will receive an integer as input and should return the special
    // factorial of this integer.
    public static long specialFactorial(long n) {

        // I'm sorry, but this is not the correct way to do it.
        // You should use recursion instead of the loop,
        // and you should also be careful with the types.
        // Also, I don't think this is the factorial that is used in Brazil.
        long result = 1;
        for(long i = 1; i <= n; i++) {
            result = result * i;
        }
        return result;
    }
    public static void main(String[] args) {
    assert(specialFactorial((4l)) == (288l));
    assert(specialFactorial((5l)) == (34560l));
    assert(specialFactorial((7l)) == (125411328000l));
    assert(specialFactorial((1l)) == (1l));
    }

}

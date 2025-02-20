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

        long factorial = 1;
        for(long i = n; i > 0; i--){
            factorial *= i;
        }
        for(long i = n-1; i > 0; i--){
            factorial *= i;
        }
        for(long i = n-2; i > 0; i--){
            factorial *= i;
        }
        for(long i = n-3; i > 0; i--){
            factorial *= i;
        }
        for(long i = n-4; i > 0; i--){
            factorial *= i;
        }
        return factorial;
    }
    public static void main(String[] args) {
    assert(specialFactorial((4l)) == (288l));
    assert(specialFactorial((5l)) == (34560l));
    assert(specialFactorial((7l)) == (125411328000l));
    assert(specialFactorial((1l)) == (1l));
    }

}

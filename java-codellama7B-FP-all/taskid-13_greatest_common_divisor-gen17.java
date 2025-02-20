import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return a greatest common divisor of two integers a and b
    // >>> greatestCommonDivisor((3l), (5l))
    // (1l)
    // >>> greatestCommonDivisor((25l), (15l))
    // (5l)
    public static long greatestCommonDivisor(long a, long b) {

        // if a == 0 or b == 0, gcd is the other number
        if ((a == 0) || (b == 0)) {
            return (a + b);
        }
        // repeat until either a or b is zero
        while ((a != 0) && (b != 0)) {
            // if a > b, a = a mod b
            if (a > b) {
                a = a % b;
            } else {
                // else b = b mod a
                b = b % a;
            }
        }
        // return the non-zero number
        return (a + b);
    }
    public static void main(String[] args) {
    assert(greatestCommonDivisor((3l), (7l)) == (1l));
    assert(greatestCommonDivisor((10l), (15l)) == (5l));
    assert(greatestCommonDivisor((49l), (14l)) == (7l));
    assert(greatestCommonDivisor((144l), (60l)) == (12l));
    }

}

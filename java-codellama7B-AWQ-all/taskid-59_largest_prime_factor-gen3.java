import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return the largest prime factor of n. Assume n > 1 and is not a prime.
    // >>> largestPrimeFactor((13195l))
    // (29l)
    // >>> largestPrimeFactor((2048l))
    // (2l)
    public static long largestPrimeFactor(long n) {

        // Initially, set the prime factor to 1.
        long primeFactor = 1l;
        // Loop until n is divided by 2 or n is 1.
        while (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) {
            // If n is divisible by 2, divide n by 2 and set prime factor to 2.
            if (n % 2 == 0) {
                n /= 2;
                primeFactor = 2l;
            // If n is divisible by 3, divide n by 3 and set prime factor to 3.
            } else if (n % 3 == 0) {
                n /= 3;
                primeFactor = 3l;
            // If n is divisible by 5, divide n by 5 and set prime factor to 5.
            } else if (n % 5 == 0) {
                n /= 5;
                primeFactor = 5l;
            }
        }
        return primeFactor;
    }
    public static void main(String[] args) {
    assert(largestPrimeFactor((15l)) == (5l));
    assert(largestPrimeFactor((27l)) == (3l));
    assert(largestPrimeFactor((63l)) == (7l));
    assert(largestPrimeFactor((330l)) == (11l));
    assert(largestPrimeFactor((13195l)) == (29l));
    }

}

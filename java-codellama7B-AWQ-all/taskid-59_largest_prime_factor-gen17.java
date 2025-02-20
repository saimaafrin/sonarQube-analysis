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

        // Factor n as (a * b)
        long a = 0;
        long b = 0;
        for (long i = 1; i <= n; ++i) {
            // If i divides n then a and b are factors of n
            if (n % i == 0) {
                // Return i if it is prime
                if (isPrime(i)) {
                    return i;
                }
                // a and b are factors of n
                a = i;
                b = n / i;
                break;
            }
        }
        // If a and b are factors of n then return the larger of a and b
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
    public static void main(String[] args) {
    assert(largestPrimeFactor((15l)) == (5l));
    assert(largestPrimeFactor((27l)) == (3l));
    assert(largestPrimeFactor((63l)) == (7l));
    assert(largestPrimeFactor((330l)) == (11l));
    assert(largestPrimeFactor((13195l)) == (29l));
    }

}

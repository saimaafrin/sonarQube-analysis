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

        if (n % 2 == 0) {
            return largestPrimeFactor(n / 2);
        }
        if (n % 3 == 0) {
            return largestPrimeFactor(n / 3);
        }
        if (n % 5 == 0) {
            return largestPrimeFactor(n / 5);
        }
        if (n % 7 == 0) {
            return largestPrimeFactor(n / 7);
        }
        if (n % 11 == 0) {
            return largestPrimeFactor(n / 11);
        }
        if (n % 13 == 0) {
            return largestPrimeFactor(n / 13);
        }
        if (n % 17 == 0) {
            return largestPrimeFactor(n / 17);
        }
        if (n % 19 == 0) {
            return largestPrimeFactor(n / 19);
        }
        if (n % 23 == 0) {
            return largestPrimeFactor(n / 23);
        }
        if (n % 29 == 0) {
            return largestPrimeFactor(n / 29);
        }
        return n;
    }
    public static void main(String[] args) {
    assert(largestPrimeFactor((15l)) == (5l));
    assert(largestPrimeFactor((27l)) == (3l));
    assert(largestPrimeFactor((63l)) == (7l));
    assert(largestPrimeFactor((330l)) == (11l));
    assert(largestPrimeFactor((13195l)) == (29l));
    }

}

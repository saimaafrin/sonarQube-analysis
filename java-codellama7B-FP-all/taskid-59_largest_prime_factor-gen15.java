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

        int i = 0;
        while (n % 2 == 0) {
            n /= 2;
            i++;
        }
        while (n % 3 == 0) {
            n /= 3;
            i++;
        }
        while (n % 5 == 0) {
            n /= 5;
            i++;
        }
        while (n % 7 == 0) {
            n /= 7;
            i++;
        }
        while (n % 11 == 0) {
            n /= 11;
            i++;
        }
        while (n % 13 == 0) {
            n /= 13;
            i++;
        }
        while (n % 17 == 0) {
            n /= 17;
            i++;
        }
        while (n % 19 == 0) {
            n /= 19;
            i++;
        }
        while (n % 23 == 0) {
            n /= 23;
            i++;
        }
        while (n % 29 == 0) {
            n /= 29;
            i++;
        }
        return (long)(Math.pow(10, i));
    }
    public static void main(String[] args) {
    assert(largestPrimeFactor((15l)) == (5l));
    assert(largestPrimeFactor((27l)) == (3l));
    assert(largestPrimeFactor((63l)) == (7l));
    assert(largestPrimeFactor((330l)) == (11l));
    assert(largestPrimeFactor((13195l)) == (29l));
    }

}

import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // For a given number n, find the largest number that divides n evenly, smaller than n
    // >>> largestDivisor((15l))
    // (5l)
    public static long largestDivisor(long n) {

        if (n == 1) return 1;
        long[] primes = SieveOfEratosthenes(n);
        long[] factors = new long[primes.length];
        int k = 0;
        for (long p : primes)
            factors[k++] = p;
        Arrays.sort(factors);
        long result = 1;
        for (long f : factors)
            if (n % f == 0) {
                result = f;
                break;
            }
        return result;
    }
    public static void main(String[] args) {
    assert(largestDivisor((3l)) == (1l));
    assert(largestDivisor((7l)) == (1l));
    assert(largestDivisor((10l)) == (5l));
    assert(largestDivisor((100l)) == (50l));
    assert(largestDivisor((49l)) == (7l));
    }

}

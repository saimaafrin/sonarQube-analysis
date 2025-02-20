import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return array list of prime factors of given integer in the order from smallest to largest.
    // Each of the factors should be array listed number of times corresponding to how many times it appeares in factorization.
    // Input number should be equal to the product of all factors
    // >>> factorize((8l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)2l, (long)2l)))
    // >>> factorize((25l))
    // (new ArrayList<Long>(Arrays.asList((long)5l, (long)5l)))
    // >>> factorize((70l))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)5l, (long)7l)))
    public static ArrayList<Long> factorize(long n) {

        // This is the list that we will return
        ArrayList<Long> factors = new ArrayList<Long>();
        long currentFactor = 2l;
        // We need to divide n by currentFactor until it is smaller than currentFactor
        // This means we can get the factors of n
        while (n > 1l) {
            // This is the number of times we can divide n by currentFactor
            long divisors = 0l;
            // This is the largest possible divisor
            // To find divisor we divide n by currentFactor and see if it is greater than 1
            while (n > 1l && (n % currentFactor) == 0l) {
                n /= currentFactor;
                divisors++;
            }
            // The factors are added to the list
            for (long i = 0l; i < divisors; i++) {
                factors.add(currentFactor);
            }
            // We are going to the next factor
            currentFactor++;
        }
        // We need to be sure that currentFactor is not equal to 1
        // We want to know if the number is prime
        if (n == 1l) {
            factors.add(n);
        }
        // We return the factors
        return factors;
    }
    public static void main(String[] args) {
    assert(factorize((2l)).equals((new ArrayList<Long>(Arrays.asList((long)2l)))));
    assert(factorize((4l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)2l)))));
    assert(factorize((8l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)2l, (long)2l)))));
    assert(factorize((57l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)19l)))));
    assert(factorize((3249l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)19l, (long)19l)))));
    assert(factorize((185193l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l, (long)19l, (long)19l, (long)19l)))));
    assert(factorize((20577l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)19l, (long)19l, (long)19l)))));
    assert(factorize((18l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)3l)))));
    }

}

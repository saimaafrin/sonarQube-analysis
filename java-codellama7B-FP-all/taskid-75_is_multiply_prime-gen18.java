import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that returns true if the given number is the multiplication of 3 prime numbers
    // and false otherwise.
    // Knowing that (a) is less then 100. 
    // Example:
    // >>> isMultiplyPrime((30l))
    // (true)
    // 30 = 2 * 3 * 5
    public static boolean isMultiplyPrime(long a) {

        if (a < 3 || a % 2 == 0 || a % 3 == 0 || a % 5 == 0) return false;

        long[] factors = new long[a - 1];
        int i = 0;
        factors[i] = 2;
        while (i < factors.length) {
            ++i;
            factors[i] = factors[i - 1] + 1;
            long potentialFactor = factors[i];
            if (isPrime(potentialFactor)) {
                if (isPrime(potentialFactor * 2)) {
                    factors[i] = potentialFactor * 2;
                    return factors[i] == a;
                } else if (isPrime(potentialFactor * 3)) {
                    factors[i] = potentialFactor * 3;
                    return factors[i] == a;
                } else if (isPrime(potentialFactor * 5)) {
                    factors[i] = potentialFactor * 5;
                    return factors[i] == a;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
    assert(isMultiplyPrime((5l)) == (false));
    assert(isMultiplyPrime((30l)) == (true));
    assert(isMultiplyPrime((8l)) == (true));
    assert(isMultiplyPrime((10l)) == (false));
    assert(isMultiplyPrime((125l)) == (true));
    assert(isMultiplyPrime((105l)) == (true));
    assert(isMultiplyPrime((126l)) == (false));
    assert(isMultiplyPrime((729l)) == (false));
    assert(isMultiplyPrime((891l)) == (false));
    assert(isMultiplyPrime((1001l)) == (true));
    }

}

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

        if (a < 100) {
            return false;
        }
        long[] factors = new long[a];
        int i = 2;
        while (i * i <= a) {
            if (a % i == 0) {
                factors[i] = 1;
                int i2 = i * 2;
                while (i2 <= a) {
                    factors[i2] = 1;
                    i2 = i2 + i;
                }
            }
            i = i + 1;
        }
        int nfact = 0;
        for (int f : factors) {
            if (f == 0) {
                nfact += 1;
            }
        }
        if (nfact == 3) {
            return true;
        } else {
            return false;
        }
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

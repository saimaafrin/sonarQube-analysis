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

        long[] primes = new long[100];
        long[] factors = new long[100];
        int primeCounter = 0;
        for(int i = 2; i < a; i++) {
            if(isPrime(i) && primeCounter < 100) {
                primes[primeCounter] = i;
                factors[primeCounter] = 1;
                primeCounter++;
            }
        }
        for(int i = 0; i < primeCounter; i++) {
            for(int j = i + 1; j < primeCounter; j++) {
                if((a % primes[i] == 0) && (a % primes[j] == 0)) {
                    return true;
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

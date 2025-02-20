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

        // This is a classic problem for number theory
        // the easiest way to solve this problem is to use prime factorization
        // first check if the number is prime
        if(a > 1) {
            // find the prime factorization of the number
            // factorize(a) -> Pair<List<Long>, List<Long>>
            // the first list is the prime factorization
            Pair<List<Long>, List<Long>> factor = Utils.factorize(a);
            // check if there is only two prime numbers
            // if so, we can divide the number with the first prime and the second prime
            // if the result is greater then 1, then it's not a multiply of three prime numbers
            // if the result is 1, then we have the solution, else the number is not a multiply of three prime numbers
            if(factor.getValue0().size() == 2) {
                Long f = factor.getValue0().get(0);
                Long s = factor.getValue0().get(1);
                // if the result is not 1, then the number is not a multiply of three prime numbers
                if(a / f / s > 1) {
                    return false;
                } else {
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

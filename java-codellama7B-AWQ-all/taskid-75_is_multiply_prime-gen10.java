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

        long a1 = 2;
        long a2 = 3;
        long a3 = 5;
        long a4 = 7;
        long a5 = 11;
        long a6 = 13;
        long a7 = 17;
        long a8 = 19;
        long a9 = 23;
        long a10 = 29;
        if (a < 2) {
            return false;
        }
        if (a % a1 == 0 && a % a2 == 0 && a % a3 == 0) {
            return true;
        }
        if (a % a4 == 0 && a % a5 == 0 && a % a6 == 0) {
            return true;
        }
        if (a % a7 == 0 && a % a8 == 0 && a % a9 == 0) {
            return true;
        }
        if (a % a10 == 0 && a % a4 == 0 && a % a9 == 0) {
            return true;
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

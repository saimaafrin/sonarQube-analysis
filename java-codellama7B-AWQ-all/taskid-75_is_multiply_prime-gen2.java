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

        long aSquare = (long)Math.pow(a, 2);
        long aCube = (long)Math.pow(a, 3);
        long aFourth = (long)Math.pow(a, 4);
        long aFifth = (long)Math.pow(a, 5);
        long aSixth = (long)Math.pow(a, 6);
        long aSeventh = (long)Math.pow(a, 7);
        long aEighth = (long)Math.pow(a, 8);
        long aNinth = (long)Math.pow(a, 9);
        long aTenth = (long)Math.pow(a, 10);
        long aEleventh = (long)Math.pow(a, 11);
        long aTwelfth = (long)Math.pow(a, 12);
        long aThirteenth = (long)Math.pow(a, 13);
        long aFourteenth = (long)Math.pow(a, 14);
        long aFifteenth = (long)Math.pow(a, 15);
        long aSixteenth = (long)Math.pow(a, 16);
        long aSeventeenth = (long)Math.pow(a, 17);
        long aEighteenth = (long)Math.pow(a, 18);
        long aNineteenth = (long)Math.pow(a, 19);
        long aTwenty = (long)Math.pow(a, 20);
        long aTwentyFirst = (long)Math.pow(a, 21);
        long aTwentySecond = (long)Math.pow(a, 22);
        long aTwentyThird = (long)Math.pow(a, 23);
        long aTwentyForth = (long)Math.pow(a, 24);
        long aTwentyFifth = (long)Math.pow(a, 25);
        long aTwentySixth = (long)Math.pow(a, 26);
        long aTwentySeventh = (long)Math.pow(a, 27);
        long aTwentyEighth = (long)Math.pow(a, 28);
        long aTwentyNinth = (long)Math.pow(a, 29);
        long aThirty = (long)Math.pow(a, 30);
        long aThirtyFirst = (long)Math.pow(a, 31);
        long aThirtySecond = (long)Math.pow(a, 32);
        long aThirtyThird = (long)Math.pow(a, 33);
        long aThirtyFourth = (long)Math.pow(a, 34);
        long aThirtyFifth = (long)Math.pow(a, 35);
        long aThirtySixth = (long)Math.pow(a, 36);
        long aThirtySeventh = (long)Math.pow(a, 37);
        long aThirtyEighth = (long)Math.pow(a, 38);
        long aThirtyNinth = (long)Math.pow(a, 39);
        long aFourty = (long)Math.pow(a, 40);
        long aFourtyFirst = (long)Math.pow(a, 41);
        long aFourtySecond = (long)Math.pow(a, 
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

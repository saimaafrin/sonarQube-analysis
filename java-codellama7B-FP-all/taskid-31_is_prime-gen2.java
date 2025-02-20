import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return true if a given number is prime, and false otherwise.
    // >>> isPrime((6l))
    // (false)
    // >>> isPrime((101l))
    // (true)
    // >>> isPrime((11l))
    // (true)
    // >>> isPrime((13441l))
    // (true)
    // >>> isPrime((61l))
    // (true)
    // >>> isPrime((4l))
    // (false)
    // >>> isPrime((1l))
    // (false)
    public static boolean isPrime(long n) {

        // Your code goes here
        return n == 2 || n == 3 || (n > 1 && (n % 2 != 0) && (n % 3 != 0) && (n % 5 != 0) && (n % 7 != 0) && (n % 11 != 0) && (n % 13 != 0) && (n % 17 != 0) && (n % 19 != 0) && (n % 23 != 0) && (n % 29 != 0) && (n % 31 != 0) && (n % 37 != 0) && (n % 39 != 0) && (n % 41 != 0) && (n % 43 != 0) && (n % 47 != 0) && (n % 49 != 0) && (n % 53 != 0) && (n % 59 != 0) && (n % 61 != 0) && (n % 67 != 0) && (n % 71 != 0) && (n % 73 != 0) && (n % 79 != 0) && (n % 83 != 0) && (n % 89 != 0) && (n % 97 != 0));
    }
    public static void main(String[] args) {
    assert(isPrime((6l)) == (false));
    assert(isPrime((101l)) == (true));
    assert(isPrime((11l)) == (true));
    assert(isPrime((13441l)) == (true));
    assert(isPrime((61l)) == (true));
    assert(isPrime((4l)) == (false));
    assert(isPrime((1l)) == (false));
    assert(isPrime((5l)) == (true));
    assert(isPrime((11l)) == (true));
    assert(isPrime((17l)) == (true));
    assert(isPrime((85l)) == (false));
    assert(isPrime((77l)) == (false));
    assert(isPrime((255379l)) == (false));
    }

}

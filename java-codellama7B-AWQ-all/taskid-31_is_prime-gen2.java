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

        // Write your code here
        // For example, you could implement the
        // Miller-Rabin primality test:
        if (n == 1) {
            return false;
        }
        for (int i = 0; i < 100; i++) {
            if (n == 1) {
                return false;
            }
            long x = 1 + (long)(Math.random() * (n - 2));
            long d = n - 1;
            long m = 0;
            while (d % 2 == 0) {
                d = d / 2;
                m++;
            }
            long y = pow(x, d, n);
            if (y == 1 || y == n - 1) {
                continue;
            }
            for (int j = 0; j < m - 1; j++) {
                y = pow(y, 2, n);
                if (y == n - 1) {
                    break;
                }
                if (y == 1) {
                    return false;
                }
            }
            if (y != n - 1) {
                return false;
            }
        }
        return true;
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

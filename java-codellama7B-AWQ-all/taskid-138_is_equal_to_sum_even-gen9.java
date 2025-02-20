import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    // Example
    // >>> isEqualToSumEven((4l))
    // (false)
    // >>> isEqualToSumEven((6l))
    // (false)
    // >>> isEqualToSumEven((8l))
    // (true)
    public static boolean isEqualToSumEven(long n) {

        long n1 = 0;
        long n2 = 0;
        long n3 = 0;
        long n4 = 0;
        if (n % 2 == 1) return false;
        for (long i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                n1 += i;
            }
        }
        if (n == n1) return true;
        for (long i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                n2 += i;
            }
        }
        if (n == n2) return true;
        for (long i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                n3 += i;
            }
        }
        if (n == n3) return true;
        for (long i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                n4 += i;
            }
        }
        if (n == n4) return true;
        return false;
    }
    public static void main(String[] args) {
    assert(isEqualToSumEven((4l)) == (false));
    assert(isEqualToSumEven((6l)) == (false));
    assert(isEqualToSumEven((8l)) == (true));
    assert(isEqualToSumEven((10l)) == (true));
    assert(isEqualToSumEven((11l)) == (false));
    assert(isEqualToSumEven((12l)) == (true));
    assert(isEqualToSumEven((13l)) == (false));
    assert(isEqualToSumEven((16l)) == (true));
    }

}

import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, return the count of the numbers of n-digit
    // positive integers that start or end with 1.
    public static long startsOneEnds(long n) {

        if (n <= 1) return 0;
        long count = 0;
        for (int i = 2; i <= n; i++) {
            long pow = (long) Math.pow(10, i - 1);
            if (n % i == 0) {
                long left = n / i;
                long right = (n / i) - 1;
                count += (long) Math.pow(10, left) * (right + 1);
            }
        }
        return count;
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}

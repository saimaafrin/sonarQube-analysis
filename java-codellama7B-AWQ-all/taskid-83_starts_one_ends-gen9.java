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

        long ans = 0;
        if (n == 1) return 1;
        long base = 10;
        long maxVal = n;
        while (maxVal >= 1) {
            long startVal = base;
            long endVal = base;
            long endValDigits = 1;
            if (n - 2 >= 1) {
                endValDigits = n - 2;
                endVal = base * base * base * endValDigits;
            }
            endVal += endValDigits * base;
            long total = (endVal - startVal + 1);
            ans += total;
            n -= 2;
            if (n == 0) break;
            maxVal = total;
            base *= 10;
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}

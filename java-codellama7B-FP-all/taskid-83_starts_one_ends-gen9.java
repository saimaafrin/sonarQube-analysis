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

        if (n <= 1) {
            return 0;
        }
        // count the numbers that start with 1
        // there are n - 1 digits before the first 1
        // there are n - 1 digits after the first 1
        // there are n - 2 digits before the second 1
        // ...
        // there are 1 digit before the last 1
        // there are 1 digit after the last 1
        // so there are (n - 1) * (n - 1) * ... * 1
        // = (n - 1) ^ (n - 2)
        long count = 1;
        for (int i = 2; i < n; ++i) {
            count *= n - i;
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

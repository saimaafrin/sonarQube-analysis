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

        long one = n == 1 ? 1 : 0;
        long ten = n == 1 ? 0 : 10;
        long nine = n == 1 ? 0 : 9;
        long start = one + ten;
        long end = one + nine;
        long mid = ten + nine;
        long res = start + end;
        long tenDigits = ten * n;
        long nineDigits = nine * n;
        res += tenDigits * start + tenDigits * end + nineDigits * mid;
        return res;
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}

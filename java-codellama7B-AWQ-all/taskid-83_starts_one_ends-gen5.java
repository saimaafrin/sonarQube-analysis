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

        long result = 0;
        for (int i = 1; i <= n; i++) {
            int startOne = 1;
            for (int j = i; j >= 1; j--) {
                if (startOne == 0) {
                    break;
                }
                startOne = (startOne * 10) + j;
            }
            if (startOne > 0) {
                result++;
            }
            startOne = 1;
            for (int j = 1; j <= i; j++) {
                if (startOne == 0) {
                    break;
                }
                startOne = (startOne * 10) + j;
            }
            if (startOne > 0) {
                result++;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(startsOneEnds((1l)) == (1l));
    assert(startsOneEnds((2l)) == (18l));
    assert(startsOneEnds((3l)) == (180l));
    assert(startsOneEnds((4l)) == (1800l));
    assert(startsOneEnds((5l)) == (18000l));
    }

}

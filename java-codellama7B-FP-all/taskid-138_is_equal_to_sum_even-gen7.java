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

        boolean isEqual = false;
        long i = 2;
        while (i <= n / 4) {
            long j = i + 1;
            while (j <= n / 2) {
                long k = j + 1;
                while (k <= n / 2) {
                    long l = k + 1;
                    if (n == (i + j + k + l)) {
                        isEqual = true;
                        break;
                    }
                    k++;
                }
                if (isEqual) break;
                j++;
            }
            if (isEqual) break;
            i++;
        }
        return isEqual;
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

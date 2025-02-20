import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // In this problem, you will implement a function that takes two array lists of numbers,
    // and determines whether it is possible to perform an exchange of elements
    // between them to make lst1 an array array list of only even numbers.
    // There is no limit on the number of exchanged elements between lst1 and lst2.
    // If it is possible to exchange elements between the lst1 and lst2 to make
    // all the elements of lst1 to be even, return "YES".
    // Otherwise, return "NO".
    // For example:
    // >>> exchange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))), (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))))
    // ("YES")
    // >>> exchange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))), (new ArrayList<Long>(Arrays.asList((long)1l, (long)5l, (long)3l, (long)4l))))
    // ("NO")
    // It is assumed that the input array lists will be non-empty.
    public static String exchange(ArrayList<Long> lst1, ArrayList<Long> lst2) {

        boolean isEven = false;
        long tmp;
        int i = 0, j = 0;
        int n = lst1.size();
        int m = lst2.size();
        int[][] dp = new int[n + 1][m + 1];
        dp[0][0] = 1;
        for (int k = 1; k < n + 1; k++) {
            for (int q = 1; q < m + 1; q++) {
                if (lst1.get(k - 1) % 2 == 0) {
                    dp[k][q] = dp[k - 1][q];
                } else if (lst2.get(q - 1) % 2 == 0) {
                    dp[k][q] = dp[k][q - 1];
                } else {
                    dp[k][q] = dp[k - 1][q] + dp[k][q - 1];
                }
            }
        }
        for (i = n - 1; i >= 0; i--) {
            for (j = m - 1; j >= 0; j--) {
                if (dp[i][j] == 1) {
                    tmp = lst1.get(i);
                    lst1.set(i, lst2.get(j));
                    lst2.set(j, tmp);
                    break;
                }
            }
        }
        for (int k = 0; k < n; k++) {
            if (lst1.get(k) % 2 != 0) {
                isEven = false;
                break;
            } else {
                isEven = true;
            }
        }
        return isEven ? "YES" : "NO";
    }
    public static void main(String[] args) {
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))), (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))).equals(("YES")));
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))), (new ArrayList<Long>(Arrays.asList((long)1l, (long)5l, (long)3l, (long)4l)))).equals(("NO")));
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)4l, (long)3l)))).equals(("YES")));
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)5l, (long)7l, (long)3l))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)6l, (long)4l)))).equals(("YES")));
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)5l, (long)7l, (long)3l))), (new ArrayList<Long>(Arrays.asList((long)2l, (long)6l, (long)3l)))).equals(("NO")));
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)6l, (long)1l, (long)8l, (long)9l))), (new ArrayList<Long>(Arrays.asList((long)3l, (long)5l, (long)5l, (long)1l, (long)1l, (long)1l)))).equals(("NO")));
    assert(exchange((new ArrayList<Long>(Arrays.asList((long)100l, (long)200l))), (new ArrayList<Long>(Arrays.asList((long)200l, (long)200l)))).equals(("YES")));
    }

}

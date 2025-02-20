import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list arr of integers, find the minimum number of elements that
    // need to be changed to make the array array list palindromic. A palindromic array array list is an array array list that
    // is read the same backwards and forwards. In one change, you can change one element to any other element.
    // For example:
    // >>> smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)5l, (long)4l, (long)7l, (long)9l, (long)6l))))
    // (4l)
    // >>> smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)3l, (long)2l, (long)2l))))
    // (1l)
    // >>> smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)2l, (long)1l))))
    // (0l)
    public static long smallestChange(ArrayList<Long> arr) {

        if (arr.size() == 0) {
            return 0;
        }
        long minChange = Long.MAX_VALUE;
        long[] minChangeArr = new long[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            minChangeArr[i] = Long.MAX_VALUE;
        }
        for (int i = 0; i < arr.size(); i++) {
            long[] minChangeArr1 = new long[arr.size()];
            for (int j = 0; j < arr.size(); j++) {
                minChangeArr1[j] = Long.MAX_VALUE;
            }
            for (int j = 0; j < arr.size(); j++) {
                if (i == j) {
                    continue;
                }
                long change = arr.get(i) - arr.get(j);
                if (Math.abs(change) < minChangeArr[j]) {
                    minChangeArr1[j] = Math.abs(change);
                } else if (Math.abs(change) == minChangeArr[j]) {
                    minChangeArr1[j] = minChangeArr[j];
                }
            }
            for (int j = 0; j < arr.size(); j++) {
                if (minChangeArr1[j] < minChange) {
                    minChange = minChangeArr1[j];
                }
            }
        }
        return minChange;
    }
    public static void main(String[] args) {
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)5l, (long)4l, (long)7l, (long)9l, (long)6l)))) == (4l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)3l, (long)2l, (long)2l)))) == (1l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)2l)))) == (1l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)4l, (long)2l)))) == (1l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)2l, (long)1l)))) == (0l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)3l, (long)1l, (long)1l, (long)3l)))) == (0l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)1l)))) == (0l));
    assert(smallestChange((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l)))) == (1l));
    }

}

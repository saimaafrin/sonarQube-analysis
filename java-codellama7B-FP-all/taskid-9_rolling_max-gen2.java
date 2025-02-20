import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // From a given array list of integers, generate an array array list of rolling maximum element found until given moment
    // in the sequence.
    // >>> rollingMax((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)2l, (long)3l, (long)4l, (long)2l))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)3l, (long)3l, (long)4l, (long)4l)))
    public static ArrayList<Long> rollingMax(ArrayList<Long> numbers) {

        int n = numbers.size();
        ArrayList<Long> maxList = new ArrayList<Long>(Collections.nCopies(n, 0l));
        for (int i = 0; i < n; i++) {
            maxList.set(i, numbers.get(i));
        }
        for (int i = 1; i < n; i++) {
            long max = maxList.get(i);
            for (int j = i - 1; j >= 0; j--) {
                if (max < numbers.get(j)) {
                    max = numbers.get(j);
                }
                maxList.set(i, max);
            }
        }
        return maxList;
    }
    public static void main(String[] args) {
    assert(rollingMax((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(rollingMax((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(rollingMax((new ArrayList<Long>(Arrays.asList((long)4l, (long)3l, (long)2l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)4l, (long)4l, (long)4l)))));
    assert(rollingMax((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l, (long)100l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l, (long)100l, (long)100l)))));
    }

}

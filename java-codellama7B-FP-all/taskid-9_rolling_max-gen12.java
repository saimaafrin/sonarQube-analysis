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

        ArrayList<Long> max = new ArrayList<Long>();
        for (int i = 0; i < numbers.size(); i++) {
            Long value = numbers.get(i);
            if (i == 0) {
                max.add(value);
            } else {
                Long prev = max.get(i - 1);
                if (value > prev) {
                    max.add(value);
                } else {
                    max.add(prev);
                }
            }
        }
        return max;
    }
    public static void main(String[] args) {
    assert(rollingMax((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(rollingMax((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(rollingMax((new ArrayList<Long>(Arrays.asList((long)4l, (long)3l, (long)2l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)4l, (long)4l, (long)4l)))));
    assert(rollingMax((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l, (long)100l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l, (long)100l, (long)100l)))));
    }

}

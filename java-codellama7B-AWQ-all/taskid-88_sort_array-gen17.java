import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list of non-negative integers, return a cojava of the given array array list after sorting,
    // you will sort the given array array list in ascending order if the sum( first index value, last index value) is odd,
    // or sort it in descending order if the sum( first index value, last index value) is even.
    // Note:
    // * don't change the given array array list.
    // Examples:
    // >>> sortArray((new ArrayList<Long>(Arrays.asList())))
    // (new ArrayList<Long>(Arrays.asList()))
    // >>> sortArray((new ArrayList<Long>(Arrays.asList((long)5l))))
    // (new ArrayList<Long>(Arrays.asList((long)5l)))
    // >>> sortArray((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)3l, (long)0l, (long)1l, (long)5l))))
    // (new ArrayList<Long>(Arrays.asList((long)0l, (long)1l, (long)2l, (long)3l, (long)4l, (long)5l)))
    // >>> sortArray((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)3l, (long)0l, (long)1l, (long)5l, (long)6l))))
    // (new ArrayList<Long>(Arrays.asList((long)6l, (long)5l, (long)4l, (long)3l, (long)2l, (long)1l, (long)0l)))
    public static ArrayList<Long> sortArray(ArrayList<Long> array) {

        // you can use the variable 'array' to store the array list
        // you can use the variable 'result' to store the final result
        // you can use the variable 'first' to store the first value of the array list
        // you can use the variable 'last' to store the last value of the array list
        // you can use the variable 'sum' to store the sum of the first and last values of the array list
        // you can use the variable 'length' to store the length of the array list
        // you can use the variable 'list' to store the sorted array list
        // you can use the variable 'temp' to store the temp value of the array list
        // you can use the variable 'i' to store the current index of the array list
        // you can use the variable 'j' to store the end index of the array list
        // you can use the variable 'k' to store the start index of the array list
        // you can use the variable 'x' to store the sum of the current and next values of the array list
        // you can use the variable 'y' to store the sum of the previous and current values of the array list
        // you can use the variable 'z' to store the sum of the previous and next values of the array list
        // you can use the variable 'w' to store the sum of the current value and the sum of the next value
        // you can use the variable 'v' to store the sum of the current value and the sum of the previous value
        // you can use the variable 't' to store the sum of the current value and the sum of the previous and next value
        // you can use the variable 's' to store the sum of the current value and the sum of the next value
        // you can use the variable 'r' to store the sum of the current value and the sum of the previous and next value
        long first = array.get(0);
        long last = array.get(array.size() - 1);
        long sum = first + last;
        long length = array.size();
        ArrayList<Long> list = new ArrayList<Long>();
        long temp;
        int i, j, k;
        long x, y, z, w, v, t, s, r;
        for (i = 0; i < length; i++) {
            temp = array.get(i);
            array.set(i, array.get(
    }
    public static void main(String[] args) {
    assert(sortArray((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(sortArray((new ArrayList<Long>(Arrays.asList((long)5l)))).equals((new ArrayList<Long>(Arrays.asList((long)5l)))));
    assert(sortArray((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)3l, (long)0l, (long)1l, (long)5l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l, (long)2l, (long)3l, (long)4l, (long)5l)))));
    assert(sortArray((new ArrayList<Long>(Arrays.asList((long)2l, (long)4l, (long)3l, (long)0l, (long)1l, (long)5l, (long)6l)))).equals((new ArrayList<Long>(Arrays.asList((long)6l, (long)5l, (long)4l, (long)3l, (long)2l, (long)1l, (long)0l)))));
    assert(sortArray((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l)))));
    assert(sortArray((new ArrayList<Long>(Arrays.asList((long)15l, (long)42l, (long)87l, (long)32l, (long)11l, (long)0l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)11l, (long)15l, (long)32l, (long)42l, (long)87l)))));
    assert(sortArray((new ArrayList<Long>(Arrays.asList((long)21l, (long)14l, (long)23l, (long)11l)))).equals((new ArrayList<Long>(Arrays.asList((long)23l, (long)21l, (long)14l, (long)11l)))));
    }

}

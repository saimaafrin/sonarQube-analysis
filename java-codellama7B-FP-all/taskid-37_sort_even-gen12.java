import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // This function takes an array array list l and returns an array array list l' such that
    // l' is identical to l in the odd indicies, while its values at the even indicies are equal
    // to the values of the even indicies of l, but sorted.
    // >>> sortEven((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))
    // >>> sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)6l, (long)3l, (long)4l))))
    // (new ArrayList<Long>(Arrays.asList((long)3l, (long)6l, (long)5l, (long)4l)))
    public static ArrayList<Long> sortEven(ArrayList<Long> l) {

        // This function takes a long value and returns the string representation of that value.
        // >>> numberToStr(3l)
        // "3"
        // >>> numberToStr(4l)
        // "4"
        // >>> numberToStr(5l)
        // "5"
        // >>> numberToStr(6l)
        // "6"
        public static String numberToStr(long n) {
            return Long.toString(n);
        }
        // This function takes a string s and returns the long value that s represents.
        // >>> strToNumber("3")
        // 3l
        // >>> strToNumber("4")
        // 4l
        // >>> strToNumber("5")
        // 5l
        // >>> strToNumber("6")
        // 6l
        public static long strToNumber(String s) {
            return Long.parseLong(s);
        }
        ArrayList<Long> result = new ArrayList<Long>();
        int lSize = l.size();
        for (int i = 0; i < lSize; i++) {
            if (i % 2 == 0) {
                result.add(l.get(i));
            }
            else {
                long n = l.get(i);
                String s = numberToStr(n);
                long[] r = new long[strToNumber(s)];
                Arrays.sort(r);
                result.add(r[0]);
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))));
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)-10l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)5l, (long)0l, (long)9l, (long)1l, (long)123l)))));
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)8l, (long)-12l, (long)4l, (long)23l, (long)2l, (long)3l, (long)11l, (long)12l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)-12l, (long)8l, (long)3l, (long)4l, (long)5l, (long)2l, (long)12l, (long)11l, (long)23l, (long)-10l)))));
    }

}

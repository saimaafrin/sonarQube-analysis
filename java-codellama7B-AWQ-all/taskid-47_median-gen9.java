import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return median of elements in the array list l.
    // >>> median((new ArrayList<Long>(Arrays.asList((long)3l, (long)1l, (long)2l, (long)4l, (long)5l))))
    // (float)3l
    // >>> median((new ArrayList<Long>(Arrays.asList((long)-10l, (long)4l, (long)6l, (long)1000l, (long)10l, (long)20l))))
    // (15.0f)
    public static float median(ArrayList<Long> l) {

        long[] arr = l.stream().mapToLong(i->i).toArray();
        Arrays.sort(arr);
        int n = arr.length;
        if ((n&1)==0) {
            return (float)(arr[n/2]+arr[n/2-1])/2;
        }
        return (float)arr[n/2];
    }
    public static void main(String[] args) {
    assert(median((new ArrayList<Long>(Arrays.asList((long)3l, (long)1l, (long)2l, (long)4l, (long)5l)))) == (float)3l);
    assert(median((new ArrayList<Long>(Arrays.asList((long)-10l, (long)4l, (long)6l, (long)1000l, (long)10l, (long)20l)))) == (8.0f));
    assert(median((new ArrayList<Long>(Arrays.asList((long)5l)))) == (float)5l);
    assert(median((new ArrayList<Long>(Arrays.asList((long)6l, (long)5l)))) == (5.5f));
    assert(median((new ArrayList<Long>(Arrays.asList((long)8l, (long)1l, (long)3l, (long)9l, (long)9l, (long)2l, (long)7l)))) == (float)7l);
    }

}

import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return maximum element in the array list.
    // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (3l)
    // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l))))
    // (123l)
    public static long maxElement(ArrayList<Long> l) {

        // Return maximum element in the array list.
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
        // (3l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l))))
        // (123l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l))))
        // (2l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l))))
        // (2l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l))))
        // (3l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l))))
        // (3l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l, (long)-4l))))
        // (3l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l, (long)-4l, (long)-5l))))
        // (5l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l, (long)-4l, (long)-5l, (long)6l))))
        // (6l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l, (long)-4l, (long)-5l, (long)6l, (long)-7l))))
        // (6l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l, (long)-4l, (long)-5l, (long)6l, (long)-7l, (long)0l))))
        // (6l)
        // >>> maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)-3l, (long)-1l, (long)3l, (long)-2l, (long)-4l, (long)-5l, (long
    }
    public static void main(String[] args) {
    assert(maxElement((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))) == (3l));
    assert(maxElement((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)124l, (long)1l, (long)-10l)))) == (124l));
    }

}

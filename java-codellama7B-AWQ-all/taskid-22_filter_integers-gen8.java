import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Filter given array list of any javathon values only for integers
    // >>> filterIntegers((new ArrayList<Object>(Arrays.asList((String)"a", (String)3.14f, (String)5l))))
    // (new ArrayList<Long>(Arrays.asList((long)5l)))
    // >>> filterIntegers((new ArrayList<Object>(Arrays.asList(1l, 2l, 3l, "abc", new HashMap<Long,Long>(Map.of()), new ArrayList<Long>(Arrays.asList())))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))
    public static ArrayList<Long> filterIntegers(ArrayList<Object> values) {

        // This is the arraylist that we will return
        ArrayList<Long> retList = new ArrayList<>();

        // Iterate through the input arraylist
        for(Object value : values) {
            // Check if the current value is an integer
            // If the current value is not an integer, then we will skip this iteration and move on
            // to the next one.
            if(!value.getClass().equals(Long.class)) {
                continue;
            }

            // If the current value is an integer, then we will add it to the retList
            retList.add((long) value);
        }

        // Return the filtered retList
        return retList;
    }
    public static void main(String[] args) {
    assert(filterIntegers((new ArrayList<Object>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(filterIntegers((new ArrayList<Object>(Arrays.asList(4l, new HashMap<Long,Long>(Map.of()), new ArrayList<Long>(Arrays.asList()), 23.2f, 9l, "adasd")))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)9l)))));
    assert(filterIntegers((new ArrayList<Object>(Arrays.asList(3l, "c", 3l, 3l, "a", "b")))).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)3l, (long)3l)))));
    }

}

import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return sorted unique elements in an array array list
    // >>> unique((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)5l, (long)2l, (long)3l, (long)3l, (long)9l, (long)0l, (long)123l))))
    // (new ArrayList<Long>(Arrays.asList((long)0l, (long)2l, (long)3l, (long)5l, (long)9l, (long)123l)))
    public static ArrayList<Long> unique(ArrayList<Long> l) {

        // Sort the array
        l.sort(Long::compare);
        // Initialize a temp array list
        ArrayList<Long> temp = new ArrayList<>();
        // Initialize a new array list
        ArrayList<Long> res = new ArrayList<>();
        // Loop over the array list
        for (int i = 0; i < l.size(); i++) {
            if (temp.isEmpty()) {
                temp.add(l.get(i));
            } else if (l.get(i) != temp.get(temp.size() - 1)) {
                temp.add(l.get(i));
            }
        }
        // Add the unique elements to the result
        res.addAll(temp);
        return res;
    }
    public static void main(String[] args) {
    assert(unique((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)5l, (long)2l, (long)3l, (long)3l, (long)9l, (long)0l, (long)123l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)2l, (long)3l, (long)5l, (long)9l, (long)123l)))));
    }

}

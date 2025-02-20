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

        // sort elements in an array list
        Collections.sort(l);
        // create a new array list to store the unique elements
        ArrayList<Long> u = new ArrayList<Long>();
        // add the first element to unique array list
        u.add(l.get(0));
        // compare each element with the previous element
        for (int i = 1; i < l.size(); i++) {
            Long n = l.get(i);
            Long p = u.get(u.size() - 1);
            if (!n.equals(p)) {
                u.add(n);
            }
        }
        return u;
    }
    public static void main(String[] args) {
    assert(unique((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)5l, (long)2l, (long)3l, (long)3l, (long)9l, (long)0l, (long)123l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)2l, (long)3l, (long)5l, (long)9l, (long)123l)))));
    }

}

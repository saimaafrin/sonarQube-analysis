import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given array list of integers, return array list in strange order.
    // Strange sorting, is when you start with the minimum value,
    // then maximum of the remaining integers, then minimum and so on.
    // Examples:
    // >>> strangeSortList((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)2l, (long)3l)))
    // >>> strangeSortList((new ArrayList<Long>(Arrays.asList((long)5l, (long)5l, (long)5l, (long)5l))))
    // (new ArrayList<Long>(Arrays.asList((long)5l, (long)5l, (long)5l, (long)5l)))
    // >>> strangeSortList((new ArrayList<Long>(Arrays.asList())))
    // (new ArrayList<Long>(Arrays.asList()))
    public static ArrayList<Long> strangeSortList(ArrayList<Long> lst) {

        if (lst.size() == 0) {
            return lst;
        }
        ArrayList<Long> ret = new ArrayList<Long>();
        long min = Collections.min(lst);
        ret.add(min);
        lst.remove(new Integer(lst.indexOf(min)));
        if (lst.size() == 0) {
            return ret;
        }
        long max = Collections.max(lst);
        ret.add(max);
        lst.remove(new Integer(lst.indexOf(max)));
        if (lst.size() == 0) {
            return ret;
        }
        while (lst.size() > 0) {
            long next = min;
            for (long l : lst) {
                if (l < next) {
                    next = l;
                }
            }
            ret.add(next);
            lst.remove(new Integer(lst.indexOf(next)));
        }
        return ret;
    }
    public static void main(String[] args) {
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)4l, (long)2l, (long)3l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)5l, (long)6l, (long)7l, (long)8l, (long)9l)))).equals((new ArrayList<Long>(Arrays.asList((long)5l, (long)9l, (long)6l, (long)8l, (long)7l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)5l, (long)2l, (long)4l, (long)3l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)5l, (long)6l, (long)7l, (long)8l, (long)9l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)9l, (long)5l, (long)8l, (long)6l, (long)7l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)5l, (long)5l, (long)5l, (long)5l)))).equals((new ArrayList<Long>(Arrays.asList((long)5l, (long)5l, (long)5l, (long)5l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l, (long)7l, (long)8l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)8l, (long)2l, (long)7l, (long)3l, (long)6l, (long)4l, (long)5l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)0l, (long)2l, (long)2l, (long)2l, (long)5l, (long)5l, (long)-5l, (long)-5l)))).equals((new ArrayList<Long>(Arrays.asList((long)-5l, (long)5l, (long)-5l, (long)5l, (long)0l, (long)2l, (long)2l, (long)2l)))));
    assert(strangeSortList((new ArrayList<Long>(Arrays.asList((long)111111l)))).equals((new ArrayList<Long>(Arrays.asList((long)111111l)))));
    }

}

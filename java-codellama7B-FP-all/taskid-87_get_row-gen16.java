import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a 2 dimensional data, as a nested array lists,
    // which is similar to matrix, however, unlike matrices,
    // each row may contain a different number of columns.
    // Given lst, and integer x, find integers x in the array list,
    // and return array list of pairs, [(x1, y1), (x2, y2) ...] such that
    // each pair is a coordinate - (row, columns), starting with 0.
    // Sort coordinates initially by rows in ascending order.
    // Also, sort coordinates of the row by columns in descending order.
    // Examples:
    // >>> getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)1l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)1l))))), (1l))
    // (new ArrayList<Pair<Long, Long>>(Arrays.asList((Pair<Long, Long>)Pair.with(0l, 0l), (Pair<Long, Long>)Pair.with(1l, 4l), (Pair<Long, Long>)Pair.with(1l, 0l), (Pair<Long, Long>)Pair.with(2l, 5l), (Pair<Long, Long>)Pair.with(2l, 0l))))
    // >>> getRow((new ArrayList<ArrayList<Long>>(Arrays.asList())), (1l))
    // (new ArrayList<Pair<Long, Long>>(Arrays.asList()))
    // >>> getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList()), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))), (3l))
    // (new ArrayList<Pair<Long, Long>>(Arrays.asList((Pair<Long, Long>)Pair.with(2l, 2l))))
    public static ArrayList<Pair<Long, Long>> getRow(ArrayList<ArrayList<Long>> lst, long x) {

        if (lst == null || lst.size() == 0)
            return new ArrayList<Pair<Long, Long>>();
        ArrayList<Pair<Long, Long>> ans = new ArrayList<Pair<Long, Long>>();
        // get all row coordinates where x is found
        for (int i = 0; i < lst.size(); ++i) {
            ArrayList<Long> cur = lst.get(i);
            for (int j = 0; j < cur.size(); ++j) {
                if (cur.get(j) == x)
                    ans.add(Pair.with(Long.valueOf(i), Long.valueOf(j)));
            }
        }
        // sort coordinates by rows in ascending order
        ans.sort((a, b) -> {
            return a.getValue0().compareTo(b.getValue0());
        });
        // sort coordinates within each row by columns in descending order
        for (Pair<Long, Long> p : ans) {
            ArrayList<Pair<Long, Long>> tmp = new ArrayList<Pair<Long, Long>>();
            long row = p.getValue0();
            ArrayList<Long> cur = lst.get((int)row);
            for (int j = 0; j < cur.size(); ++j) {
                if (cur.get(j) == x) {
                    tmp.add(Pair.with(row, j));
                }
            }
    }
    public static void main(String[] args) {
    assert(getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)1l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)1l))))), (1l)).equals((new ArrayList<Pair<Long, Long>>(Arrays.asList((Pair<Long, Long>)Pair.with(0l, 0l), (Pair<Long, Long>)Pair.with(1l, 4l), (Pair<Long, Long>)Pair.with(1l, 0l), (Pair<Long, Long>)Pair.with(2l, 5l), (Pair<Long, Long>)Pair.with(2l, 0l))))));
    assert(getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l))))), (2l)).equals((new ArrayList<Pair<Long, Long>>(Arrays.asList((Pair<Long, Long>)Pair.with(0l, 1l), (Pair<Long, Long>)Pair.with(1l, 1l), (Pair<Long, Long>)Pair.with(2l, 1l), (Pair<Long, Long>)Pair.with(3l, 1l), (Pair<Long, Long>)Pair.with(4l, 1l), (Pair<Long, Long>)Pair.with(5l, 1l))))));
    assert(getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)1l, (long)3l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)1l, (long)4l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)1l, (long)5l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)1l, (long)6l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)1l))))), (1l)).equals((new ArrayList<Pair<Long, Long>>(Arrays.asList((Pair<Long, Long>)Pair.with(0l, 0l), (Pair<Long, Long>)Pair.with(1l, 0l), (Pair<Long, Long>)Pair.with(2l, 1l), (Pair<Long, Long>)Pair.with(2l, 0l), (Pair<Long, Long>)Pair.with(3l, 2l), (Pair<Long, Long>)Pair.with(3l, 0l), (Pair<Long, Long>)Pair.with(4l, 3l), (Pair<Long, Long>)Pair.with(4l, 0l), (Pair<Long, Long>)Pair.with(5l, 4l), (Pair<Long, Long>)Pair.with(5l, 0l), (Pair<Long, Long>)Pair.with(6l, 5l), (Pair<Long, Long>)Pair.with(6l, 0l))))));
    assert(getRow((new ArrayList<ArrayList<Long>>(Arrays.asList())), (1l)).equals((new ArrayList<Pair<Long, Long>>(Arrays.asList()))));
    assert(getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l))))), (2l)).equals((new ArrayList<Pair<Long, Long>>(Arrays.asList()))));
    assert(getRow((new ArrayList<ArrayList<Long>>(Arrays.asList((ArrayList<Long>)new ArrayList<Long>(Arrays.asList()), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l)), (ArrayList<Long>)new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))), (3l)).equals((new ArrayList<Pair<Long, Long>>(Arrays.asList((Pair<Long, Long>)Pair.with(2l, 2l))))));
    }

}

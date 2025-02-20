import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given an array array list arr of integers and a positive integer k, return a sorted array list 
    // of length k with the maximum k numbers in arr.
    // Example 1:
    // >>> maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)-4l, (long)5l))), (3l))
    // (new ArrayList<Long>(Arrays.asList((long)-4l, (long)-3l, (long)5l)))
    // Example 2:
    // >>> maximum((new ArrayList<Long>(Arrays.asList((long)4l, (long)-4l, (long)4l))), (2l))
    // (new ArrayList<Long>(Arrays.asList((long)4l, (long)4l)))
    // Example 3:
    // >>> maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)2l, (long)1l, (long)2l, (long)-1l, (long)-2l, (long)1l))), (1l))
    // (new ArrayList<Long>(Arrays.asList((long)2l)))
    // Note:
    // 1. The length of the array array list will be in the range of [1, 1000].
    // 2. The elements in the array array list will be in the range of [-1000, 1000].
    // 3. 0 <= k <= len(arr)
    public static ArrayList<Long> maximum(ArrayList<Long> arr, long k) {

        PriorityQueue<Long> maxheap = new PriorityQueue<Long>((n1, n2) -> (n1 > n2 ? 1 : 0));
        for (long i = 0; i < k; i++) {
            maxheap.add(arr.get(i));
        }
        for (long i = k; i < arr.size(); i++) {
            long n = arr.get(i);
            if (maxheap.peek() < n) {
                maxheap.poll();
                maxheap.add(n);
            }
        }
        ArrayList<Long> result = new ArrayList<Long>();
        while (!maxheap.isEmpty()) {
            result.add(0, maxheap.poll());
        }
        return result;
    }
    public static void main(String[] args) {
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)-4l, (long)5l))), (3l)).equals((new ArrayList<Long>(Arrays.asList((long)-4l, (long)-3l, (long)5l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)4l, (long)-4l, (long)4l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)4l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-3l, (long)2l, (long)1l, (long)2l, (long)-1l, (long)-2l, (long)1l))), (1l)).equals((new ArrayList<Long>(Arrays.asList((long)2l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)123l, (long)-123l, (long)20l, (long)0l, (long)1l, (long)2l, (long)-3l))), (3l)).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)20l, (long)123l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-123l, (long)20l, (long)0l, (long)1l, (long)2l, (long)-3l))), (4l)).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l, (long)2l, (long)20l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)5l, (long)15l, (long)0l, (long)3l, (long)-13l, (long)-8l, (long)0l))), (7l)).equals((new ArrayList<Long>(Arrays.asList((long)-13l, (long)-8l, (long)0l, (long)0l, (long)3l, (long)5l, (long)15l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-1l, (long)0l, (long)2l, (long)5l, (long)3l, (long)-10l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)3l, (long)5l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)1l, (long)0l, (long)5l, (long)-7l))), (1l)).equals((new ArrayList<Long>(Arrays.asList((long)5l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)4l, (long)-4l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)-4l, (long)4l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)-10l, (long)10l))), (2l)).equals((new ArrayList<Long>(Arrays.asList((long)-10l, (long)10l)))));
    assert(maximum((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)-23l, (long)243l, (long)-400l, (long)0l))), (0l)).equals((new ArrayList<Long>(Arrays.asList()))));
    }

}

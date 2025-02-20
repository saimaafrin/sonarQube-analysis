import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // "Given an array array list representing a branch of a tree that has non-negative integer nodes
    // your task is to pluck one of the nodes and return it.
    // The plucked node should be the node with the smallest even value.
    // If multiple nodes with the same smallest even value are found return the node that has smallest index.
    // The plucked node should be returned in an array array list, [ smalest_value, its index ],
    // If there are no even values or the given array array list is empty, return [].
    // Example 1:
    // >>> pluck((new ArrayList<Long>(Arrays.asList((long)4l, (long)2l, (long)3l))))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)1l)))
    // Explanation: 2 has the smallest even value, and 2 has the smallest index.
    // Example 2:
    // >>> pluck((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)1l)))
    // Explanation: 2 has the smallest even value, and 2 has the smallest index.
    // Example 3:
    // >>> pluck((new ArrayList<Long>(Arrays.asList())))
    // (new ArrayList<Long>(Arrays.asList()))
    // Example 4:
    // >>> pluck((new ArrayList<Long>(Arrays.asList((long)5l, (long)0l, (long)3l, (long)0l, (long)4l, (long)2l))))
    // (new ArrayList<Long>(Arrays.asList((long)0l, (long)1l)))
    // Explanation: 0 is the smallest value, but  there are two zeros,
    // so we will choose the first zero, which has the smallest index.
    // Constraints:
    // * 1 <= nodes.length <= 10000
    // * 0 <= node.value
    public static ArrayList<Long> pluck(ArrayList<Long> arr) {

        if(arr.size() == 0) return new ArrayList<Long>();

        // Find smallest even number
        long smallestEven = Long.MAX_VALUE;
        int smallestIndex = -1;
        int currentIndex = 0;
        for(long node : arr) {
            if(node % 2 == 0) {
                if(node < smallestEven) {
                    smallestEven = node;
                    smallestIndex = currentIndex;
                }
            }
            currentIndex++;
        }

        // Add the smallest even number to the result
        ArrayList<Long> result = new ArrayList<Long>();
        result.add(smallestEven);
        result.add((long) smallestIndex);

        // Find all indices of smallest even number
        List<Integer> indices = new ArrayList<Integer>();
        for(int i = 0; i < arr.size(); i++) {
            if(arr.get(i) == smallestEven) {
                indices.add(i);
            }
        }

        // If there are multiple indices of the smallest even number,
        // then add the smallest index to the result
        if(indices.size() > 1) {
            int smallestIndexOfSmallestEven = Integer.MAX_VALUE;
            for(int index : indices) {
                if(index < smallestIndexOfSmallestEven) {
                    smallestIndexOfSmallestEven = index;
                }
            }

            result.add((long) smallestIndexOfSmallestEven);
        }

        return result;
    }
    public static void main(String[] args) {
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)4l, (long)2l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l)))));
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l)))));
    assert(pluck((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)5l, (long)0l, (long)3l, (long)0l, (long)4l, (long)2l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)1l)))));
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)0l, (long)5l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)3l)))));
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)5l, (long)4l, (long)8l, (long)4l, (long)8l)))).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)1l)))));
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)7l, (long)6l, (long)7l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList((long)6l, (long)1l)))));
    assert(pluck((new ArrayList<Long>(Arrays.asList((long)7l, (long)9l, (long)7l, (long)1l)))).equals((new ArrayList<Long>(Arrays.asList()))));
    }

}

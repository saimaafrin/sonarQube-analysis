import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // We have an array array list 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    // numbers in the array array list will be randomly ordered. Your task is to determine if
    // it is possible to get an array array list sorted in non-decreasing order by performing 
    // the following operation on the given array array list:
    // You are allowed to perform right shift operation any number of times.
    // One right shift operation means shifting all elements of the array array list by one
    // position in the right direction. The last element of the array array list will be moved to
    // the starting position in the array array list i.e. 0th index. 
    // If it is possible to obtain the sorted array array list by performing the above operation
    // then return true else return false.
    // If the given array array list is empty then return true.
    // Note: The given array list is guaranteed to have unique elements.
    // For Example:
    // >>> moveOneBall((new ArrayList<Long>(Arrays.asList((long)3l, (long)4l, (long)5l, (long)1l, (long)2l))))
    // (true)
    // Explanation: By performin 2 right shift operations, non-decreasing order can
    // be achieved for the given array array list.
    // >>> moveOneBall((new ArrayList<Long>(Arrays.asList((long)3l, (long)5l, (long)4l, (long)1l, (long)2l))))
    // (false)
    // Explanation:It is not possible to get non-decreasing order for the given
    // array array list by performing any number of right shift operations.
    public static boolean moveOneBall(ArrayList<Long> arr) {

        if (arr.size() == 0) {
            return true;
        }
        boolean isSorted = false;
        int n = arr.size();
        int i = 0;
        while (i < n && !isSorted) {
            if (arr.get(i) > arr.get(i + 1)) {
                swap(arr, i, i + 1);
                i--;
            } else if (arr.get(i) == arr.get(i + 1)) {
                i++;
            } else {
                isSorted = true;
            }
        }
        return isSorted;
    }
    public static void main(String[] args) {
    assert(moveOneBall((new ArrayList<Long>(Arrays.asList((long)3l, (long)4l, (long)5l, (long)1l, (long)2l)))) == (true));
    assert(moveOneBall((new ArrayList<Long>(Arrays.asList((long)3l, (long)5l, (long)10l, (long)1l, (long)2l)))) == (true));
    assert(moveOneBall((new ArrayList<Long>(Arrays.asList((long)4l, (long)3l, (long)1l, (long)2l)))) == (false));
    assert(moveOneBall((new ArrayList<Long>(Arrays.asList((long)3l, (long)5l, (long)4l, (long)1l, (long)2l)))) == (false));
    assert(moveOneBall((new ArrayList<Long>(Arrays.asList()))) == (true));
    }

}

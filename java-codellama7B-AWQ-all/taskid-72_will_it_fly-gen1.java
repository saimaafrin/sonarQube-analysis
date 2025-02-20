import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that returns true if the object q will fly, and false otherwise.
    // The object q will fly if it's balanced (it is a palindromic array list) and the sum of its elements is less than or equal the maximum possible weight w.
    // Example:
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l))), (5l))
    // (false)
    // # 1+2 is less than the maximum possible weight, but it's unbalanced.
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (1l))
    // (false)
    // # it's balanced, but 3+2+3 is more than the maximum possible weight.
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (9l))
    // (true)
    // # 3+2+3 is less than the maximum possible weight, and it's balanced.
    // >>> willItFly((new ArrayList<Long>(Arrays.asList((long)3l))), (5l))
    // (true)
    // # 3 is less than the maximum possible weight, and it's balanced.
    public static boolean willItFly(ArrayList<Long> q, long w) {

        // list is empty
        if (q.isEmpty()) {
            return false;
        }
        // list has one element
        if (q.size() == 1) {
            return w >= q.get(0);
        }
        // list has more than one element
        // check if the list is balanced
        long sum = 0;
        for (long l : q) {
            sum += l;
        }
        if (sum % 2 != 0) {
            return false;
        }
        long half = sum / 2;
        // check if the list weight is less than the maximum possible weight
        return w >= half;
    }
    public static void main(String[] args) {
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (9l)) == (true));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l))), (5l)) == (false));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)3l))), (5l)) == (true));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)3l, (long)2l, (long)3l))), (1l)) == (false));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))), (6l)) == (false));
    assert(willItFly((new ArrayList<Long>(Arrays.asList((long)5l))), (5l)) == (true));
    }

}

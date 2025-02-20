import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function that takes an integer a and returns true 
    // if this ingeger is a cube of some integer number.
    // Note: you may assume the input is always valid.
    // Examples:
    // >>> iscube((1l))
    // (true)
    // >>> iscube((2l))
    // (false)
    // >>> iscube((-1l))
    // (true)
    // >>> iscube((64l))
    // (true)
    // >>> iscube((0l))
    // (true)
    // >>> iscube((180l))
    // (false)
    public static boolean iscube(long a) {

        // Use the square root method to check if a is a perfect square.
        // If it is then it must be a cube.
        // If a is a perfect square, then the formula for the square root of a
        // is the same as the formula for the cube root of a, just with 
        // the denominator being 2 instead of 3.
        // So if we can check if a is a perfect square, then we have solved the 
        // problem.
        // Let's get the square root of a and then check if it is an integer.
        long sq = (long)Math.sqrt(a);
        // If sq is not an integer then a is not a cube.
        if ((sq * sq) != a) {
            return false;
        }
        // If the square root is an integer then we can check if a is a cube by
        // computing its cube root.
        // If a/sq^2 is an integer, then a is a cube.
        // If not, then a is not a cube.
        // If a is a cube, then a/sq^2 is equal to sq.
        long cr = (long)Math.cbrt(a / (sq * sq));
        return (cr * cr * cr) == a;
    }
    public static void main(String[] args) {
    assert(iscube((1l)) == (true));
    assert(iscube((2l)) == (false));
    assert(iscube((-1l)) == (true));
    assert(iscube((64l)) == (true));
    assert(iscube((180l)) == (false));
    assert(iscube((1000l)) == (true));
    assert(iscube((0l)) == (true));
    assert(iscube((1729l)) == (false));
    }

}

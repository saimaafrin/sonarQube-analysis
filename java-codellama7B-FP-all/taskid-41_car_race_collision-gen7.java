import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Imagine a road that's a perfectly straight infinitely long line.
    // n cars are driving left to right;  simultaneously, a different set of n cars
    // are driving right to left.   The two sets of cars start out being very far from
    // each other.  All cars move in the same speed.  Two cars are said to collide
    // when a car that's moving left to right hits a car that's moving right to left.
    // However, the cars are infinitely sturdy and strong; as a result, they continue moving
    // in their trajectory as if they did not collide.
    // This function outputs the number of such collisions.
    public static long carRaceCollision(long n) {

        // This is where a dynamic programming algorithm would be used to keep track
        // of the number of collisions, but we don't need to do that; the algorithm
        // just needs to return the correct result.  To find the correct result, we
        // can count the number of pairs of cars that collide.
        long count = 0;
        for (long i = 0; i < n; i++) {
            // At each position i, if there is a car moving left to right,
            // then it will hit a car moving right to left exactly i positions
            // later.  Similarly, if there is a car moving right to left,
            // it will hit a car moving left to right exactly i positions
            // earlier.
            count += 2 * i;
        }
        return count;
    }
    public static void main(String[] args) {
    assert(carRaceCollision((2l)) == (4l));
    assert(carRaceCollision((3l)) == (9l));
    assert(carRaceCollision((4l)) == (16l));
    assert(carRaceCollision((8l)) == (64l));
    assert(carRaceCollision((10l)) == (100l));
    }

}

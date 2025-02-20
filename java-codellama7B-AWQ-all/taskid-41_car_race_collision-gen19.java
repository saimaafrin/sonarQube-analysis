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

        // This problem is the same as the ones in the previous problems.  The only difference
        // is that it's asked for the number of collisions, not the number of cars that
        // collide with each other.
        // The problem can be solved with a simple dynamic programming technique.
        // We can represent the number of collisions for n cars as a function of n-1
        // cars.  If we know the number of collisions for n-1 cars, then we can find
        // the number of collisions for n cars.  If we want to know the number of
        // collisions for n-1 cars, we can know the number of collisions for n-2 cars.
        // Therefore, we can have a dynamic programming function that takes an array of
        // long values that represent the number of collisions for n-1 cars as input.
        // The function outputs the number of collisions for n cars.
        // To solve the problem we just need to fill the array with the number of collisions
        // for n cars.
        // The problem can be solved in O(n) time and O(1) space.
        long[] collisions = new long[n + 1];
        collisions[0] = 0;
        collisions[1] = 0;
        for (int i = 2; i <= n; i++) {
            collisions[i] = i * (i - 1) / 2 * (2 * i - 1);
            for (int j = 1; j <= i - 2; j++) {
                collisions[i] += collisions[j] * collisions[i - j];
            }
        }
        return collisions[n];
    }
    public static void main(String[] args) {
    assert(carRaceCollision((2l)) == (4l));
    assert(carRaceCollision((3l)) == (9l));
    assert(carRaceCollision((4l)) == (16l));
    assert(carRaceCollision((8l)) == (64l));
    assert(carRaceCollision((10l)) == (100l));
    }

}

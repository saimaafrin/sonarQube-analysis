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

        if (n == 1) return 1;
        if (n == 2) return 3;
        if (n == 3) return 8;
        if (n == 4) return 14;
        if (n == 5) return 25;
        if (n == 6) return 41;
        if (n == 7) return 64;
        if (n == 8) return 96;
        if (n == 9) return 141;
        if (n == 10) return 214;
        if (n == 11) return 315;
        if (n == 12) return 476;
        if (n == 13) return 713;
        if (n == 14) return 1069;
        if (n == 15) return 1646;
        if (n == 16) return 2488;
        if (n == 17) return 3821;
        if (n == 18) return 6133;
        if (n == 19) return 9879;
        if (n == 20) return 15597;
        if (n == 21) return 25557;
        if (n == 22) return 42494;
        if (n == 23) return 72058;
        if (n == 24) return 120167;
        if (n == 25) return 194892;
        if (n == 26) return 303894;
        if (n == 27) return 480178;
        if (n == 28) return 785192;
        if (n == 29) return 1292687;
        if (n == 30) return 2108448;
        if (n == 31) return 3345525;
        if (n == 32) return 5393207;
        if (n == 33) return 8876616;
        if (n == 34) return 14238197;
        if (n == 35) return 23864919;
        if (n == 36) return 38932357;
        if (n == 37) return 63360739;
        if (n == 38) return 104333041;
        if (n == 39) return 171468969;
        if (n == 40) return 278927529;
        if (n == 41) return 452299643;
        if (n == 42) return 717061861;
        if (n == 43) return 1159146591;
        if (n == 44) return 1901634913;
        if (n
    }
    public static void main(String[] args) {
    assert(carRaceCollision((2l)) == (4l));
    assert(carRaceCollision((3l)) == (9l));
    assert(carRaceCollision((4l)) == (16l));
    assert(carRaceCollision((8l)) == (64l));
    assert(carRaceCollision((10l)) == (100l));
    }

}

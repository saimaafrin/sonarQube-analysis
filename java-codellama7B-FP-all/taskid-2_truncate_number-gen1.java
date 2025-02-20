import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive floating point number, it can be decomposed into
    // and integer part (largest integer smaller than given number) and decimals
    // (leftover part always smaller than 1).
    // Return the decimal part of the number.
    // >>> truncateNumber((3.5f))
    // (0.5f)
    public static float truncateNumber(float number) {

        // (Integer.MAX_VALUE - 1) = 2147483647 = 10111000011111111111111111111111
        // if a number is greater than this value it is infinity.
        // >>> (Integer.MAX_VALUE - 1)
        // 2147483647
        if (number > Integer.MAX_VALUE - 1) return 0;
        return number - (int) number;
    }
    public static void main(String[] args) {
    assert(truncateNumber((3.5f)) == (0.5f));
    assert(truncateNumber((1.25f)) == (0.25f));
    assert(truncateNumber((123.0f)) == (0.0f));
    }

}

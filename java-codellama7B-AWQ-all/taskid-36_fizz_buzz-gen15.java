import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    // >>> fizzBuzz((50l))
    // (0l)
    // >>> fizzBuzz((78l))
    // (2l)
    // >>> fizzBuzz((79l))
    // (3l)
    public static long fizzBuzz(long n) {

        return Stream.iterate(1l, x -> x + 11l).filter(x -> x < n).filter(x -> x % 13 == 0).map(x -> x / 11).filter(x -> x % 11 == 0).count();
    }
    public static void main(String[] args) {
    assert(fizzBuzz((50l)) == (0l));
    assert(fizzBuzz((78l)) == (2l));
    assert(fizzBuzz((79l)) == (3l));
    assert(fizzBuzz((100l)) == (3l));
    assert(fizzBuzz((200l)) == (6l));
    assert(fizzBuzz((4000l)) == (192l));
    assert(fizzBuzz((10000l)) == (639l));
    assert(fizzBuzz((100000l)) == (8026l));
    }

}

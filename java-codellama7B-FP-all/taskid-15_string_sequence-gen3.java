import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    // >>> stringSequence((0l))
    // ("0")
    // >>> stringSequence((5l))
    // ("0 1 2 3 4 5")
    public static String stringSequence(long n) {

        return new BigDecimal(n)
                .add(BigDecimal.ONE)
                .divide(BigDecimal.valueOf(2), 0, RoundingMode.HALF_EVEN)
                .stripTrailingZeros()
                .toPlainString()
                .replace("0.","");
    }
    public static void main(String[] args) {
    assert(stringSequence((0l)).equals(("0")));
    assert(stringSequence((3l)).equals(("0 1 2 3")));
    assert(stringSequence((10l)).equals(("0 1 2 3 4 5 6 7 8 9 10")));
    }

}

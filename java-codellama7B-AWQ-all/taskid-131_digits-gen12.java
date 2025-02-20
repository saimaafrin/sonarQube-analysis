import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, return the product of the odd digits.
    // Return 0 if all digits are even.
    // For example:
    // >>> digits((1l))
    // (1l)
    // >>> digits((4l))
    // (0l)
    // >>> digits((235l))
    // (15l)
    public static long digits(long n) {

        String s = Long.toString(n);
        String[] arr = s.split("");
        if (s.equals("")) {
            return 0;
        }
        if (s.charAt(0) % 2 == 0) {
            return 0;
        }
        List<Character> odds = Arrays.asList(arr).stream().filter(c -> Integer.parseInt(c) % 2 != 0).map(c -> c.charAt(0)).collect(Collectors.toList());
        return odds.stream().mapToLong(c -> Long.parseLong(c.toString())).reduce(1, (a, b) -> a * b);
    }
    public static void main(String[] args) {
    assert(digits((5l)) == (5l));
    assert(digits((54l)) == (5l));
    assert(digits((120l)) == (1l));
    assert(digits((5014l)) == (5l));
    assert(digits((98765l)) == (315l));
    assert(digits((5576543l)) == (2625l));
    assert(digits((2468l)) == (0l));
    }

}

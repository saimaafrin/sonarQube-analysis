import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Your task is to implement a function that will simplify the expression
    // x * n. The function returns true if x * n evaluates to a whole number and false
    // otherwise. Both x and n, are string representation of a fraction, and have the following format,
    // <numerator>/<denominator> where both numerator and denominator are positive whole numbers.
    // You can assume that x, and n are valid fractions, and do not have zero as denominator.
    // >>> simplify(("1/5"), ("5/1"))
    // (true)
    // >>> simplify(("1/6"), ("2/1"))
    // (false)
    // >>> simplify(("7/10"), ("10/2"))
    // (false)
    public static boolean simplify(String x, String n) {

        int[] xDenNumeratorDenominator = x.split("/")[1].split("/")[0].split("/").length;
        int[] nDenNumeratorDenominator = n.split("/")[1].split("/")[0].split("/").length;
        int[] xNumeratorDenominator = Arrays.stream(x.split("/")).mapToInt(Integer::parseInt).toArray();
        int[] nNumeratorDenominator = Arrays.stream(n.split("/")).mapToInt(Integer::parseInt).toArray();
        int gcd = gcd(xNumeratorDenominator[0], xNumeratorDenominator[1]);
        int gcd1 = gcd(nNumeratorDenominator[0], nNumeratorDenominator[1]);
        int denominator = (xNumeratorDenominator[1]*nNumeratorDenominator[1])/gcd1;
        if(xDenNumeratorDenominator == 1 && nDenNumeratorDenominator == 1){
            return true;
        }else{
            return (xNumeratorDenominator[0]*nNumeratorDenominator[1])/gcd == (xNumeratorDenominator[1]*nNumeratorDenominator[0])/gcd;
        }
    }
    public static void main(String[] args) {
    assert(simplify(("1/5"), ("5/1")) == (true));
    assert(simplify(("1/6"), ("2/1")) == (false));
    assert(simplify(("5/1"), ("3/1")) == (true));
    assert(simplify(("7/10"), ("10/2")) == (false));
    assert(simplify(("2/10"), ("50/10")) == (true));
    assert(simplify(("7/2"), ("4/2")) == (true));
    assert(simplify(("11/6"), ("6/1")) == (true));
    assert(simplify(("2/3"), ("5/2")) == (false));
    assert(simplify(("5/2"), ("3/5")) == (false));
    assert(simplify(("2/4"), ("8/4")) == (true));
    assert(simplify(("2/4"), ("4/2")) == (true));
    assert(simplify(("1/5"), ("5/1")) == (true));
    assert(simplify(("1/5"), ("1/5")) == (false));
    }

}

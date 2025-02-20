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

        String[] xNumerator = x.split("/")[0].split("");
        String[] xDenominator = x.split("/")[1].split("");
        String[] nNumerator = n.split("/")[0].split("");
        String[] nDenominator = n.split("/")[1].split("");
        Integer xNumeratorSum = Arrays.stream(xNumerator).map(Integer::parseInt).sum();
        Integer xDenominatorSum = Arrays.stream(xDenominator).map(Integer::parseInt).sum();
        Integer nNumeratorSum = Arrays.stream(nNumerator).map(Integer::parseInt).sum();
        Integer nDenominatorSum = Arrays.stream(nDenominator).map(Integer::parseInt).sum();
        // System.out.println(xNumeratorSum + " / " + xDenominatorSum);
        // System.out.println(nNumeratorSum + " / " + nDenominatorSum);
        Integer gcd = gcd(xNumeratorSum, xDenominatorSum, nNumeratorSum, nDenominatorSum);
        // System.out.println(gcd);
        String xMultipliedByNumerator = (xNumeratorSum / gcd) + "/" + (xDenominatorSum / gcd);
        String nMultipliedByDenominator = (nNumeratorSum / gcd) + "/" + (nDenominatorSum / gcd);
        // System.out.println(xMultipliedByNumerator + " * " + nMultipliedByDenominator);
        Integer xMultipliedByNumeratorSum = Arrays.stream(xMultipliedByNumerator.split("/")[0].split("")).map(Integer::parseInt).sum();
        Integer xMultipliedByNumeratorDenominator = Arrays.stream(xMultipliedByNumerator.split("/")[1].split("")).map(Integer::parseInt).sum();
        // System.out.println(xMultipliedByNumeratorSum);
        // System.out.println(xMultipliedByNumeratorDenominator);
        Integer nMultipliedByDenominatorSum = Arrays.stream(nMultipliedByDenominator.split("/")[0].split("")).map(Integer::parseInt).sum();
        Integer nMultipliedByDenominatorDenominator = Arrays.stream(nMultipliedByDenominator.split("/")[1].split("")).map(Integer::parseInt).sum();
        // System.out.println(nMultipliedByDenominatorSum);
        // System.out.println(nMultipliedByDenominatorDenominator);
        return xMultipliedByNumeratorSum * nMultipliedByDenominatorDenominator == xMultipliedByNumeratorDenominator * nMultipliedByDenominatorSum;
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

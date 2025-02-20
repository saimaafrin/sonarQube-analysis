import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // This function takes two positive numbers x and y and returns the
    // biggest even integer number that is in the range [x, y] inclusive. If 
    // there's no such number, then the function should return -1.
    // For example:
    // >>> chooseNum((12l), (15l))
    // (14l)
    // >>> chooseNum((13l), (12l))
    // (-1l)
    public static long chooseNum(long x, long y) {

        // Complete the function
        // DO NOT write main() function.
        // DO NOT read any input, instead use the arguments to the function.
        // DO NOT print anything.
        // DO NOT use any temporary arrays, instead use the arguments to the function.
        // DO NOT use any libraries or functions that are not part of the standard Java API.
        // DO NOT use any loops.
        // DO NOT use any additional variables, just the arguments passed to the function.
        // TIP: Check the sign of the numbers x and y to determine if you need to subtract or add.
        long ans = -1;
        if (x % 2 == 0 && y % 2 == 0) {
            if (y >= x) {
                ans = y;
                long mid = x + (y - x) / 2;
                while (mid >= x && mid <= y) {
                    if (mid % 2 == 0) {
                        ans = mid;
                        break;
                    }
                    mid += (y - x) / 2;
                }
            }
        }
        return ans;
    }
    public static void main(String[] args) {
    assert(chooseNum((12l), (15l)) == (14l));
    assert(chooseNum((13l), (12l)) == (-1l));
    assert(chooseNum((33l), (12354l)) == (12354l));
    assert(chooseNum((5234l), (5233l)) == (-1l));
    assert(chooseNum((6l), (29l)) == (28l));
    assert(chooseNum((27l), (10l)) == (-1l));
    assert(chooseNum((7l), (7l)) == (-1l));
    assert(chooseNum((546l), (546l)) == (546l));
    }

}

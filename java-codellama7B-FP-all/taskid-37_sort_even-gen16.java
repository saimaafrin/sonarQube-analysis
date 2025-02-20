import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // This function takes an array array list l and returns an array array list l' such that
    // l' is identical to l in the odd indicies, while its values at the even indicies are equal
    // to the values of the even indicies of l, but sorted.
    // >>> sortEven((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l))))
    // (new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))
    // >>> sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)6l, (long)3l, (long)4l))))
    // (new ArrayList<Long>(Arrays.asList((long)3l, (long)6l, (long)5l, (long)4l)))
    public static ArrayList<Long> sortEven(ArrayList<Long> l) {

        // This variable is a list of the even indices of the arraylist
        ArrayList<Integer> evenIndices = new ArrayList<Integer>();
        // This variable is a list of the odd indices of the arraylist
        ArrayList<Integer> oddIndices = new ArrayList<Integer>();
        // This variable is the size of the arraylist
        int size = l.size();
        // This for loop populates the two lists mentioned above
        for (int i = 0; i < size; i++) {
            if (i % 2 == 0) {
                evenIndices.add(i);
            } else {
                oddIndices.add(i);
            }
        }
        // This for loop populates the variable which will be returned
        ArrayList<Long> result = new ArrayList<Long>();
        // This for loop goes through all of the indices of the arraylist
        for (int i = 0; i < size; i++) {
            // If this index is even
            if (i % 2 == 0) {
                // This variable is the index of the element of the arraylist at the same index
                int index = evenIndices.get(i);
                // This variable is the element of the arraylist at the same index
                long element = l.get(index);
                // This list is a list of all of the elements of the arraylist at the even indicies
                ArrayList<Long> elements = new ArrayList<Long>();
                // This for loop populates the variable mentioned above
                for (int j = 0; j < size; j++) {
                    if (evenIndices.get(j) == index) {
                        elements.add(l.get(j));
                    }
                }
                // This method sorts the list of elements
                Collections.sort(elements);
                // This for loop adds all of the elements of the sorted list to the result variable
                for (int j = 0; j < elements.size(); j++) {
                    result.add(elements.get(j));
                }
                // This adds the element to the result variable
                result.add(element);
            }
            // If this index is odd
            else {
                // This variable is the index of the element of the arraylist at the same index
                int index = oddIndices.get(i);
                // This variable is the element of the arraylist at the same index
                long element = l.get(index);
                // This adds the element to the result variable
                result.add(element);
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l)))));
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)9l, (long)0l, (long)123l, (long)1l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)-10l, (long)3l, (long)-5l, (long)2l, (long)-3l, (long)3l, (long)5l, (long)0l, (long)9l, (long)1l, (long)123l)))));
    assert(sortEven((new ArrayList<Long>(Arrays.asList((long)5l, (long)8l, (long)-12l, (long)4l, (long)23l, (long)2l, (long)3l, (long)11l, (long)12l, (long)-10l)))).equals((new ArrayList<Long>(Arrays.asList((long)-12l, (long)8l, (long)3l, (long)4l, (long)5l, (long)2l, (long)12l, (long)11l, (long)23l, (long)-10l)))));
    }

}

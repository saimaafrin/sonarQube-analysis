import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given array list of numbers (of at least two elements), apply a linear transform to that array list,
    // such that the smallest number will become 0 and the largest will become 1
    // >>> rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)2.0f, (float)3.0f, (float)4.0f, (float)5.0f))))
    // (new ArrayList<Float>(Arrays.asList((float)0.0f, (float)0.25f, (float)0.5f, (float)0.75f, (float)1.0f)))
    public static ArrayList<Float> rescaleToUnit(ArrayList<Float> numbers) {

        // Sort the numbers in ascending order
        numbers.sort(Comparator.naturalOrder());
        // Initialize a new array list to hold the transformed numbers
        ArrayList<Float> result = new ArrayList<Float>();
        // Initialize the index to the second element in the original list
        int index = 1;
        // Loop through the list until the end of the list
        while (index < numbers.size()) {
            // Initialize the current element's value to the next element in the list
            float current = numbers.get(index);
            // Subtract the current element's value from the next element's value
            // This will be the difference between the two elements
            float diff = numbers.get(index+1) - current;
            // Divide the difference by the size of the list
            diff = diff / numbers.size();
            // Add the difference to the current element's value
            current += diff;
            // Add the current element's value to the transformed list
            result.add(current);
            // Increment the index by two to move through the list by two elements at a time
            index += 2;
        }
        // Return the transformed list of numbers
        return result;
    }
    public static void main(String[] args) {
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)2.0f, (float)49.9f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.0f, (float)1.0f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)100.0f, (float)49.9f)))).equals((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)0.0f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)2.0f, (float)3.0f, (float)4.0f, (float)5.0f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.0f, (float)0.25f, (float)0.5f, (float)0.75f, (float)1.0f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)2.0f, (float)1.0f, (float)5.0f, (float)3.0f, (float)4.0f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.25f, (float)0.0f, (float)1.0f, (float)0.5f, (float)0.75f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)12.0f, (float)11.0f, (float)15.0f, (float)13.0f, (float)14.0f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.25f, (float)0.0f, (float)1.0f, (float)0.5f, (float)0.75f)))));
    }

}

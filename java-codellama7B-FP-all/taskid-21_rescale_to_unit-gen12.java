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

        // sort numbers in ascending order, find largest and smallest number
        numbers.sort(Float::compare);
        float min = numbers.get(0);
        float max = numbers.get(numbers.size() - 1);
        // divide number range by 10000, then multiply the result by the difference between the largest and the smallest number,
        // then add the smallest number to the result.
        // if max == min, return 0 as the smallest number.
        return numbers.stream()
            .map(number -> number == max ? 1.0f : (((number - min) / (max - min)) * (max - min) + min))
            .collect(Collectors.toCollection(ArrayList::new));
    }
    public static void main(String[] args) {
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)2.0f, (float)49.9f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.0f, (float)1.0f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)100.0f, (float)49.9f)))).equals((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)0.0f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)1.0f, (float)2.0f, (float)3.0f, (float)4.0f, (float)5.0f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.0f, (float)0.25f, (float)0.5f, (float)0.75f, (float)1.0f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)2.0f, (float)1.0f, (float)5.0f, (float)3.0f, (float)4.0f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.25f, (float)0.0f, (float)1.0f, (float)0.5f, (float)0.75f)))));
    assert(rescaleToUnit((new ArrayList<Float>(Arrays.asList((float)12.0f, (float)11.0f, (float)15.0f, (float)13.0f, (float)14.0f)))).equals((new ArrayList<Float>(Arrays.asList((float)0.25f, (float)0.0f, (float)1.0f, (float)0.5f, (float)0.75f)))));
    }

}

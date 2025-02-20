import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input to this function is a string representing musical notes in a special ASCII format.
    // Your task is to parse this string and return array list of integers corresponding to how many beats does each
    // not last.
    // Here is a legend:
    // 'o' - whole note, lasts four beats
    // 'o|' - half note, lasts two beats
    // '.|' - quater note, lasts one beat
    // >>> parseMusic(("o o| .| o| o| .| .| .| .| o o"))
    // (new ArrayList<Long>(Arrays.asList((long)4l, (long)2l, (long)1l, (long)2l, (long)2l, (long)1l, (long)1l, (long)1l, (long)1l, (long)4l, (long)4l)))
    public static ArrayList<Long> parseMusic(String music_string) {

        // Please take a look at the provided examples to see how the string is formatted.
        // Also, please take a look at the provided examples to see how the list of integers is formatted.
        // We hope that you will be able to implement this function correctly.
        // If you need help, here is a hint:
        // 1. You will need a data structure to store the state of your parsing so far.
        // 2. You should have two methods: one that will "eat" one character at a time and return true if you are done, and
        // false if you need to continue eating.
        // 3. Once you have finished eating, you should return an integer that represents the number of beats the last
        // note you consumed was worth.
        // 4. If you are given the string "o o| .| o| o| .| .| .| .| o o", the output should be [4,2,1,2,2,1,1,1,1,4,4].
        // This is because:
        // 'o' - whole note, lasts four beats
        // 'o|' - half note, lasts two beats
        // '.|' - quater note, lasts one beat
        // 5. You should check to make sure that the input string is valid.
        // 6. You should also check to make sure that your output list has the correct length.
        // 7. If the output list is not the correct length, your function should return null.
        // If the input string is invalid, your function should return null.

        ArrayList<Long> result = new ArrayList<>();
        long beatLength = 4;
        if (music_string.length() == 0) {
            return result;
        }
        if (music_string.charAt(0) == 'o') {
            beatLength = 4;
            music_string = music_string.substring(1);
        }
        else if (music_string.charAt(0) == 'o|') {
            beatLength = 2;
            music_string = music_string.substring(2);
        }
        else if (music_string.charAt(0) == '.|') {
            beatLength = 1;
            music_string = music_string.substring(2);
        }
        else {
            return null;
        }
        for (int i = 0; i < music_string.length(); i++) {
            char c = music_string.charAt(i);
            if (c == 'o') {
                result.add(beatLength);
                beatLength = 4;
                music_string = music_string.substring(i + 1);
                i = -1;
            }
            else if (c == 'o|') {
                result.add(beatLength);
                beatLength = 2;
                music_string = music_string.substring(i + 1);
                i = -1;
            }
            else if (c == '.|') {
                result.add(beatLength);
                beatLength = 1;
                music_string = music_string.substring(i
    }
    public static void main(String[] args) {
    assert(parseMusic(("")).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(parseMusic(("o o o o")).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)4l, (long)4l, (long)4l)))));
    assert(parseMusic((".| .| .| .|")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)1l, (long)1l, (long)1l)))));
    assert(parseMusic(("o| o| .| .| o o o o")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)2l, (long)1l, (long)1l, (long)4l, (long)4l, (long)4l, (long)4l)))));
    assert(parseMusic(("o| .| o| .| o o| o o|")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)2l, (long)1l, (long)4l, (long)2l, (long)4l, (long)2l)))));
    }

}

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

        String[] notes = music_string.split("");
        int length = notes.length;
        ArrayList<Long> result = new ArrayList<Long>();
        for (int i = 0; i < length; i++) {
            switch (notes[i]) {
                case 'o':
                    result.add((long) 4);
                    break;
                case 'o|':
                    result.add((long) 2);
                    break;
                case '.|':
                    result.add((long) 1);
                    break;
            }
        }
        return result;
    }
    public static void main(String[] args) {
    assert(parseMusic(("")).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(parseMusic(("o o o o")).equals((new ArrayList<Long>(Arrays.asList((long)4l, (long)4l, (long)4l, (long)4l)))));
    assert(parseMusic((".| .| .| .|")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)1l, (long)1l, (long)1l)))));
    assert(parseMusic(("o| o| .| .| o o o o")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)2l, (long)1l, (long)1l, (long)4l, (long)4l, (long)4l, (long)4l)))));
    assert(parseMusic(("o| .| o| .| o o| o o|")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)1l, (long)2l, (long)1l, (long)4l, (long)2l, (long)4l, (long)2l)))));
    }

}

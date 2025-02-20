import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You will be given the name of a class (a string) and an array array list of extensions.
    // The extensions are to be used to load additional classes to the class. The
    // strength of the extension is as follows: Let CAP be the number of the uppercase
    // letters in the extension's name, and let SM be the number of lowercase letters 
    // in the extension's name, the strength is given by the fraction CAP - SM. 
    // You should find the strongest extension and return a string in this 
    // format: ClassName.StrongestExtensionName.
    // If there are two or more extensions with the same strength, you should
    // choose the one that comes first in the array list.
    // For example, if you are given "Slices" as the class and an array array list of the
    // extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    // return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    // (its strength is -1).
    // Example:
    // >>> StrongestExtension(("my_class"), (new ArrayList<String>(Arrays.asList((String)"AA", (String)"Be", (String)"CC"))))
    // ("my_class.AA")
    public static String StrongestExtension(String class_name, ArrayList<String> extensions) {

        int max_value = -1;
        int max_index = -1;
        for (int i = 0; i < extensions.size(); i++) {
            int count_upper = 0;
            int count_lower = 0;
            for (int j = 0; j < extensions.get(i).length(); j++) {
                if (extensions.get(i).charAt(j) >= 65 && extensions.get(i).charAt(j) <= 90) {
                    count_upper++;
                }
                else if (extensions.get(i).charAt(j) >= 97 && extensions.get(i).charAt(j) <= 122) {
                    count_lower++;
                }
            }
            int value = count_upper - count_lower;
            if (value > max_value) {
                max_value = value;
                max_index = i;
            }
            else if (value == max_value && i < max_index) {
                max_index = i;
            }
        }
        if (max_index == -1) {
            return "";
        }
        return (class_name + "." + extensions.get(max_index));
    }
    public static void main(String[] args) {
    assert(StrongestExtension(("Watashi"), (new ArrayList<String>(Arrays.asList((String)"tEN", (String)"niNE", (String)"eIGHt8OKe")))).equals(("Watashi.eIGHt8OKe")));
    assert(StrongestExtension(("Boku123"), (new ArrayList<String>(Arrays.asList((String)"nani", (String)"NazeDa", (String)"YEs.WeCaNe", (String)"32145tggg")))).equals(("Boku123.YEs.WeCaNe")));
    assert(StrongestExtension(("__YESIMHERE"), (new ArrayList<String>(Arrays.asList((String)"t", (String)"eMptY", (String)"nothing", (String)"zeR00", (String)"NuLl__", (String)"123NoooneB321")))).equals(("__YESIMHERE.NuLl__")));
    assert(StrongestExtension(("K"), (new ArrayList<String>(Arrays.asList((String)"Ta", (String)"TAR", (String)"t234An", (String)"cosSo")))).equals(("K.TAR")));
    assert(StrongestExtension(("__HAHA"), (new ArrayList<String>(Arrays.asList((String)"Tab", (String)"123", (String)"781345", (String)"-_-")))).equals(("__HAHA.123")));
    assert(StrongestExtension(("YameRore"), (new ArrayList<String>(Arrays.asList((String)"HhAas", (String)"okIWILL123", (String)"WorkOut", (String)"Fails", (String)"-_-")))).equals(("YameRore.okIWILL123")));
    assert(StrongestExtension(("finNNalLLly"), (new ArrayList<String>(Arrays.asList((String)"Die", (String)"NowW", (String)"Wow", (String)"WoW")))).equals(("finNNalLLly.WoW")));
    assert(StrongestExtension(("_"), (new ArrayList<String>(Arrays.asList((String)"Bb", (String)"91245")))).equals(("_.Bb")));
    assert(StrongestExtension(("Sp"), (new ArrayList<String>(Arrays.asList((String)"671235", (String)"Bb")))).equals(("Sp.671235")));
    }

}

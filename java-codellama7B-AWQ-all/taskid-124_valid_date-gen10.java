import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You have to write a function which validates a given date string and
    // returns true if the date is valid otherwise false.
    // The date is valid if all of the following rules are satisfied:
    // 1. The date string is not empty.
    // 2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    // 3. The months should not be less than 1 or higher than 12.
    // 4. The date should be in the format: mm-dd-yyyy
    // >>> validDate(("03-11-2000"))
    // (true)
    // >>> validDate(("15-01-2012"))
    // (false)
    // >>> validDate(("04-0-2040"))
    // (false)
    // >>> validDate(("06-04-2020"))
    // (true)
    // >>> validDate(("06/04/2020"))
    // (false)
    public static boolean validDate(String date) {

        String[] parts = date.split("-");
        if(parts.length != 3)
            return false;

        String month = parts[0];
        String day = parts[1];
        String year = parts[2];

        int dayNum;
        int monthNum;

        try {
            dayNum = Integer.parseInt(day);
            monthNum = Integer.parseInt(month);
        } catch (NumberFormatException e) {
            return false;
        }

        if(monthNum < 1 || monthNum > 12)
            return false;

        boolean is29feb = monthNum == 2 && dayNum == 29;
        boolean is31days = monthNum == 3 || monthNum == 5 || monthNum == 8 || monthNum == 10;
        boolean is30days = monthNum == 4 || monthNum == 6 || monthNum == 9 || monthNum == 11;

        if(is29feb) {
            if(year.length() != 4)
                return false;
            if(dayNum < 1 || dayNum > 29)
                return false;
        } else if(is31days) {
            if(dayNum < 1 || dayNum > 31)
                return false;
        } else if(is30days) {
            if(dayNum < 1 || dayNum > 30)
                return false;
        } else {
            if(dayNum < 1 || dayNum > 31)
                return false;
        }

        return true;
    }
    public static void main(String[] args) {
    assert(validDate(("03-11-2000")) == (true));
    assert(validDate(("15-01-2012")) == (false));
    assert(validDate(("04-0-2040")) == (false));
    assert(validDate(("06-04-2020")) == (true));
    assert(validDate(("01-01-2007")) == (true));
    assert(validDate(("03-32-2011")) == (false));
    assert(validDate(("")) == (false));
    assert(validDate(("04-31-3000")) == (false));
    assert(validDate(("06-06-2005")) == (true));
    assert(validDate(("21-31-2000")) == (false));
    assert(validDate(("04-12-2003")) == (true));
    assert(validDate(("04122003")) == (false));
    assert(validDate(("20030412")) == (false));
    assert(validDate(("2003-04")) == (false));
    assert(validDate(("2003-04-12")) == (false));
    assert(validDate(("04-2003")) == (false));
    }

}

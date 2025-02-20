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

        String[] dateParts = date.split("-");
        // Check month format
        if(!(dateParts[0].matches("[0-1]{1}[0-9]{1}")))
            return false;

        // Check date format
        if(!(dateParts[1].matches("[0-3]{1}[0-9]{1}")))
            return false;

        // Check year format
        if(!(dateParts[2].matches("\\d{4}")))
            return false;

        // Check month range
        if(!(Integer.parseInt(dateParts[0]) >= 1 && Integer.parseInt(dateParts[0]) <= 12))
            return false;

        // Check date range
        if(!(Integer.parseInt(dateParts[1]) >= 1 && Integer.parseInt(dateParts[1]) <= 31))
            return false;

        // Check if date is 29, 30 or 31
        int year = Integer.parseInt(dateParts[2]);
        int month = Integer.parseInt(dateParts[0]);
        int date = Integer.parseInt(dateParts[1]);
        boolean isLeapYear = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
        if(month == 2){
            if(date < 1 || date > 28){
                return false;
            }
            else if(date > 28){
                if(!isLeapYear)
                    return false;
            }
        }
        else if(month == 4 || month == 6 || month == 9 || month == 11){
            if(date < 1 || date > 30)
                return false;
        }
        else if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
            if(date < 1 || date > 31)
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

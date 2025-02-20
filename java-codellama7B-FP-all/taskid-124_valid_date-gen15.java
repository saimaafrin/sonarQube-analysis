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

        // Your code goes here
        //check whether the date is empty
        if(date.length()==0)
            return false;

        //check whether the date has - or /
        if(!date.contains("-") && !date.contains("/"))
            return false;

        //check whether the date has - or /
        if(date.contains("-")){
            //split the date based on -
            String[] parts=date.split("-");

            //check whether the date has 3 parts
            if(parts.length!=3)
                return false;

            //check whether the year is valid
            if(parts[2].length()>4)
                return false;
        }
        else{
            //split the date based on /
            String[] parts=date.split("/");

            //check whether the date has 3 parts
            if(parts.length!=3)
                return false;

            //check whether the year is valid
            if(parts[2].length()>4)
                return false;
        }

        //check whether the day is valid
        if(parts[1].length()>2)
            return false;

        //check whether the month is valid
        if(parts[0].length()>2)
            return false;

        //check whether the year is valid
        if(parts[2].length()!=4)
            return false;

        //check whether the month is less than 1 or greater than 12
        int month=Integer.parseInt(parts[0]);
        if(month<1 || month>12)
            return false;

        //check whether the year is less than 1900 or greater than 2020
        int year=Integer.parseInt(parts[2]);
        if(year<1900 || year>2020)
            return false;

        //check whether the month and year is valid
        if(!validMonthAndYear(month,year))
            return false;

        //check whether the day is valid
        int day=Integer.parseInt(parts[1]);
        if(!validDay(month,day,year))
            return false;

        //check whether the date is valid
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

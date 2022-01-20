Vowel Count
import java.util.Arrays;
public class Vowels {

  public static int getCount(String str) {
    int vowelsCount = 0;

     for(char c : str.toCharArray())
      vowelsCount += (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') ? 1 : 0;

    return vowelsCount;

  }


  }


Grasshopper - Summation
public class GrassHopper {

    public static int summation(int n) {
      int result = 0 ;

        for (int i = 0; i<=n ; i++ ){
          result +=i;
        }
        return result;
    }
}
Sum Arrays
public class SumArray {

  public static double sum(double[] numbers) {
    if (numbers.length == 0){ return 0 ;}
     double result = 0;
    for (double num : numbers ){
      result += num;
    }
    return result ;
  }
}

Remove First and Last Character
public class RemoveChars {
    public static String remove(String str) {
      String newstring =str.substring(1,(str.length()-1));
      return  newstring ;
        // your code here
    }
}

Return Negative
public class Kata {

  public static int makeNegative(final int x) {
    if (x>= 0){
    int chenger = x * 2;
    return (x - chenger); // Your code here.
    }
    return x;
  }

}
Sum of positive
public class Positive{

  public static int sum(int[] arr){
    int nums2 = 0;

    for (int i : arr ){
      if (i > 0){
        nums2+=i;
      }

    }


    return nums2;
  }

}
Multiply
public class Multiply {
    public static Double multiply(Double a, Double b) {
        return a * b;
    }
}
Even or Odd
public class EvenOrOdd {
    public static String even_or_odd(int number) {
      if (number %2 == 0){
        return "Even";
      }
      return "Odd";
    }
}

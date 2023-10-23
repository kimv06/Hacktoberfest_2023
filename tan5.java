import java.util.*;

public class HappyNum {
    public static int isNumHappy(int num) {
        int rem = 0, sum = 0;
        // calculate the sum of squares of each digit
        while (num > 0) {
            rem = num % 10;
            sum = sum + (rem * rem);
            num = num / 10;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        // Take num
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number greater than 0:");
        int num = sc.nextInt();
        int finalVal = num;
        while (finalVal != 1 && finalVal != 4) {
            finalVal = isNumHappy(finalVal);
        }
        if (finalVal == 1) {
            System.out.println("The number entered is a Happy Number");
        } else {
            System.out.println(" The number entered is not a Happy Number");
        }
    }
}

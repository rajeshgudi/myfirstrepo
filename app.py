// Save this file as SumCalculator.java
import java.util.Scanner; 

public class SumCalculator {
    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your first number: ");
        int num1 = scanner.nextInt();

        System.out.print("Enter your second number: ");
        int num2 = scanner.nextInt();

        // Calculate and display the result
        int sum = num1 + num2;
        System.out.println("The sum of " + num1 + " and " + num2 + " is: " + sum);

        // Close the scanner to prevent memory leaks
        scanner.close();
    }
}

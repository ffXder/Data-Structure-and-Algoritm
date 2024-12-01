import java.util.Stack;
import java.util.Scanner;

public class FruitBasket {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Stack basket = new Stack();

        System.out.println("Catch and eat any of these fruits:('apple', 'orange', 'mango', 'guava')");
        System.out.print("How many fruits would you like to catch? ");
        int countFruits = input.nextInt(); // counts how many fruit it will catch
        input.nextLine(); // creates new line to avoid scanner overlapping

        System.out.println("Choose a fruit to catch. Press A, O, M, or G.");

        for (int i = 0; i < countFruits; i++) {
            System.out.print("Fruits " + (i + 1) + " of " + countFruits + ": ");
            String catchFruit = input.nextLine().toUpperCase();

            switch (catchFruit) {
                case "A":
                    basket.push("apple"); // add fruit in stack
                    break;
                case "O":
                    basket.push("orange");
                    break;
                case "M":
                    basket.push("mango");
                    break;
                case "G":
                    basket.push("guava");
                    break;
                default:
                    System.out.println("fruit cannot be catch in the basket!");
            }
        }
        System.out.println("Your basket now has: " + basket);

        for (int i = 0; i < countFruits + 1; i++) {
            System.out.print("Press E to eat a fruit. ");
            String eatFruit = input.nextLine();

            if (eatFruit.equalsIgnoreCase("E")) {
                basket.pop(); // remove fruit in stack
                if (basket.isEmpty()) {
                    System.out.println("No more fruits");
                    break;
                } else {
                    System.out.print("Eating " + basket.peek() + " nomnom! ");
                    System.out.println("Fruit(s) in the basket: " + basket);
                }
            }
        }
    }
}

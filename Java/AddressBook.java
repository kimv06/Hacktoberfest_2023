/* In this application, users can store and manage contacts with their names and phone numbers. 
 * They can add new contacts, view existing contacts, and search for a contact by name.
 */

import java.util.HashMap;
import java.util.Scanner;

public class AddressBook {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<String, String> contacts = new HashMap<>();

        while (true) {
            System.out.println("Address Book Menu:");
            System.out.println("1. Add Contact");
            System.out.println("2. View Contacts");
            System.out.println("3. Search Contact");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume the newline character after nextInt()

            switch (choice) {
                case 1:
                    System.out.print("Enter contact name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter contact phone number: ");
                    String phoneNumber = scanner.nextLine();
                    contacts.put(name, phoneNumber);
                    System.out.println("Contact added successfully!");
                    break;
                case 2:
                    if (contacts.isEmpty()) {
                        System.out.println("No contacts found.");
                    } else {
                        System.out.println("Contacts:");
                        for (String contactName : contacts.keySet()) {
                            String contactNumber = contacts.get(contactName);
                            System.out.println(contactName + ": " + contactNumber);
                        }
                    }
                    break;
                case 3:
                    System.out.print("Enter contact name to search: ");
                    String searchName = scanner.nextLine();
                    if (contacts.containsKey(searchName)) {
                        String contactNumber = contacts.get(searchName);
                        System.out.println("Contact found: " + searchName + ": " + contactNumber);
                    } else {
                        System.out.println("Contact not found.");
                    }
                    break;
                case 4:
                    System.out.println("Exiting address book. Goodbye!");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}

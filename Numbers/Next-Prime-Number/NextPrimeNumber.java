package net.bethydiakabana.project.numbers;

import java.util.Scanner;

public class NextPrimeNumber {
	private static boolean isPrime(int n) {
		if (n % 2 == 0)
			return false;
		for (int i = 3; i*i <= n; i+=2) {
			if (n % i == 0) 
				return false;
		} // end for
		return true;
	} // end method isPrime

	public static void main(String[] args) {
		try(Scanner scanner = new Scanner(System.in)) {
			System.out.print("Enter a number: ");
			int n = scanner.nextInt();
			String answer = "y";
			
			while(answer.equals("y")) {
				if (isPrime(++n)) {
					System.out.println(n + " is the next prime.");
					System.out.print("Would you like to find the next prime? (y/n): ");
					answer = scanner.next();
				} else {
					continue;
				} // end if
			} // end while
			System.out.println("See you soon!");
		} // end try-with-resource
	} // end main
} // end class NextPrimeNumber

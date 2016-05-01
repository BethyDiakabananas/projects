package net.bethydiakabana.project.numbers;

import java.util.ArrayList;
import java.util.List;

public class Fibonacci {
	/**
	 * Returns a <tt>List</tt> of n fibonacci numbers
	 * <p>
	 * <b>NOTE:</b> This is used for unit testing purposes as oppose to a void,
	 * or a simplereturn
	 * 
	 * @param n
	 *            the number of integers in fibonacci sequence
	 * @return a <tt>List</tt> containing n fibonacci numbers
	 */
	public List<Integer> fibonacciIterative(int n) {
		List<Integer> fibonacciSequence = new ArrayList<Integer>(n);
		int fibonacciNumber = 0;
		for (int i = 1; i <= n; i++) {
			fibonacciNumber = (int) (((Math.pow((1 + Math.sqrt(5)), i) - Math.pow((1 - Math.sqrt(5)), i))
					/ (Math.pow(2, i) * Math.sqrt(5))));
			fibonacciSequence.add(fibonacciNumber);
		} // end for
		return fibonacciSequence;
	} // end method fibonacci

	/**
	 * Returns the nth fibonacci integer in a fibonacci sequence
	 * 
	 * @param n
	 *            the nth integer in a fibonacci sequence
	 * @return the nth integer in a fibonacci sequence
	 */
	public int fibonacciRecursive(int n) {
		if (n <= 1)
			return n;
		else
			return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
	} // end method fibonacciRecursive
} // end class fibonacciNumber

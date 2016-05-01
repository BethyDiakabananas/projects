package net.bethydiakabana;

public class PrimeFactorization {
	public static void findPrimeFactorization(long N) {
		// uses exponents for efficiency
		for (int i = 2; i * i <= N; i++) {
			// continues to divide through if i is a factor of N
			while (N % i == 0) {
				System.out.print(i + " ");
				N = N / i;
			} // end while
		} // end for

		// if the biggest factor occurs only once
		if (N > 1)
			System.out.println(N);
		else
			System.out.println();
	} // end method findPrimeFactorization
} // end PrimeFactorization

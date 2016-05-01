package net.bethydiakabana.project.numbers;

public class PrimeFactorization {
	public static void findPrimeFactorization(long N) {
		for (int i = 2; i * i <= N; i++) {
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

} // end PrimeFactorization

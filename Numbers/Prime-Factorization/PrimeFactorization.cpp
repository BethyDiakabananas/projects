#include <stdio.h>
#include <iostream>
using namespace std;

void findPrimeFactorization(int n);

int main() {
	int n;
	cout << "Enter a number to factor: ";
	cin >> n;
	findPrimeFactorization(n);

	return 0;
}
// finds prime factorization
void findPrimeFactorization(int n) {
	for (int i = 2; i * i <= n; i++) {
		while (n % i == 0) {
			printf("%d ", i);
			n /= i;
		} // end while
	} // end for

	if (n > 1)
		printf("%d\n", n);
	else
		printf("\n");
}

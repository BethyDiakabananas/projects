(defun fibonacci(n)
	(check-type n (integer 1 *) "a positive integer")
	(if < n 2) n
	(+ (fib (- n 1) (fib ( - n 2)))))

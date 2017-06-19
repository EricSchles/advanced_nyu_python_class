How to refactor your code
	* What we will refactor:
		https://github.com/EricSchles/investigator
	* How to read code:
		https://github.com/aredridel/how-to-read-code/blob/master/how-to-read-code.md
	* A fairly hard codebase to understand:
		https://github.com/openopps/openopps-platform
		try praticing reading code here.
	* full blown example with tasking:
		* https://github.com/18F/openFEC
		* Nice intro to tasking: https://www.confluent.io/blog/introduction-to-apache-kafka-for-python-programmers/ - kafka
Recursion

How to write a recursive function:

With the fibonnaci sequence algorithm as an example:


Step 1:
	Specify the base case - THIS MUST ALWAYS COME FIRST
	The reason why we specify a base case, is because this is how the recursion ends.

	A base case is a part of the flow of control of the recursive function call where the
	function does not return another function.  It can either return nothing or return a number or 
	some other object.  

	Example:

	def fib(n):
		if n == 0:
			return 1
		if n == 1:
			return 1

Step 2:
	Part 1)
		Specify the recursive calls that will be made - This is the main work of the function.

		def fib(n):
			if n == 0:
				return 1
			if n == 1:
				return 1
			else:
				return fib() + fib()
	Part 2)
		Specify the parameters to be passed to the recursive step.  

		def fib(n):
			if n == 0:
				return 1
			if n == 1:
				return 1
			else:
				return fib(n-1) + fib(n-2)

Reference:
	https://en.wikipedia.org/wiki/Fibonacci_number

Project Review:

https://github.com/EricSchles/deployable
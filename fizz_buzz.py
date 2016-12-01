def fizz_buzz(num):
	#Return FizzBuzz if num is divisible by both 3 and 5
	if num % 3 == 0 and num % 5 == 0:
		return 'FizzBuzz'

	#Returns Buzz if num is divisible by 5
	elif num % 5 == 0:
		return 'Buzz'

	#Returns Fizz if num is divisible by 3
	elif num % 3 == 0:
		return 'Fizz'

	#Returns num itself if it is not divisible by either 3 or 5
	else:
		return num
